import os
import requests

from dotenv import load_dotenv

load_dotenv()


params = {
    'key': os.environ['TRELLO_KEY'],
    'token': os.environ['TRELLO_TOKEN']
}

def get_my_id(params):
    url = "https://api.trello.com/1/members/me"
    
    r = requests.get(url, params={'key':params['key'], 'token':params['token']})
    
    return r.json()['id']

def get_list_id(name, board_id, params):
    url = f"https://api.trello.com/1/boards/{board_id}/lists/"
    
    r = requests.get(url, params={'key':params['key'], 'token':params['token']})
    list_ids = [x['id'] for x in r.json() if x['name'] == name]
    
    if list_ids:
        return list_ids[0]
    else:
        return False

def get_board_id(name, params):
    url = "https://api.trello.com/1/members/me/boards"
    
    r = requests.get(url, params={'key':params['key'], 'token':params['token']})
    ids = [x['id'] for x in r.json() if x['name'] == name]
    
    if ids:
        return ids[0]
    else:
        return False

def get_my_cards_in_list(board_name, list_name, params):
    my_id = get_my_id(params)
    board_id = get_board_id(board_name, params)
    list_id = get_list_id(list_name, board_id, params)
    
    url = f"https://api.trello.com/1/boards/{board_id}/cards"
    r = requests.get(url, params={'key':params['key'], 'token':params['token']})
    my_cards = [x for x in r.json() if x['idList'] == list_id and my_id in x['idMembers']]

    return my_cards


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--board_name', '-b', help="Trello board name", type=str)
    parser.add_argument('--list_name', '-l', help="Trello list name", type=str)
    args = parser.parse_args()

    cards = get_my_cards_in_list(
        board_name=args.board_name,
        list_name=args.list_name,
        params=params
    )

    for i in cards:
        print(i['name'], '\n', i['shortUrl'], '\n', sep='')