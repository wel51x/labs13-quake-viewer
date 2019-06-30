# Research

USGS does not capture all earthquakes, particularly below 4.5 mag: https://earthquake.usgs.gov/data/comcat/data-availability.php

## Concepts
* [Omori's law, Båth's law, and Gutenberg–Richter law](https://en.wikipedia.org/wiki/Aftershock#Aftershock_size_and_frequency_with_time)

## Discussion
* [Kaggle](https://www.kaggle.com/usgs/earthquake-database) Significant Earthquakes, 1965-2016
    * **Data:** USGS magnitude 5.5+
* [Kaggle](https://www.kaggle.com/c/LANL-Earthquake-Prediction) contest to predict earthquakes from simulated lab data
    * **Data:** simulated lab data
    * [1st Place Solution](https://www.kaggle.com/c/LANL-Earthquake-Prediction/discussion/94390#latest-550455)
    * [YouTube walkthrough](https://www.youtube.com/watch?v=TffGdSsWKlA)

## Articles
* *"Exploring the fascinating world of incomplete seismicity data"*
    * [Part I: Bayesian inference](https://medium.com/the-history-risk-forecast-of-perils/exploring-the-fascinating-world-of-incomplete-seismicity-data-part-i-ii-bayesian-inference-386338b43b71)
    * [Part II: Mixture Modelling](https://medium.com/the-history-risk-forecast-of-perils/exploring-the-fascinating-world-of-incomplete-seismicity-data-part-ii-ii-mixture-modelling-5d2665cb9fa3)

## Publications

### [Developing an expert system based on association rules and predicate logic for earthquake prediction](http://isiarticles.com/bundles/Article/pre/pdf/52598.pdf)
* **Date:** November 2014
* **Data:** whole-world data
* **problem:** 
* *incomplete article access*

### [Short Term Earthquake Prediction in Hindukush Region using Tree based Ensemble Learning](https://www.researchgate.net/publication/314203623_Short_Term_Earthquake_Prediction_in_Hindukush_Region_Using_Tree_Based_Ensemble_Learning)
**Date:** December 2016

>The study period for this work is selected from January, 1980 to January 2016. The earthquake catalog is obtained from US Geological Survey and is publically available [15]. The catalog must be evaluated for completeness magnitude or cut-off magnitude (Mc). Mc is defined as the minimum reported magnitude, above which the catalog is considered to be complete. There are different methods available in literate, which can be used for finding Mc [16]. The earthquakes listed in catalog below cut-off magnitude are removed before employing for feature calculation. Mc is calculated through visual examination of frequency magnitude distribution of events [17]

>These classification models are capable of predicting earthquakes of magnitude 5.0 and above for the horizon of 15 days

>There are total of 51 seismic features calculated for earthquake prediction in this study.

### [Earthquake prediction model using support vector regressor and hybrid neural networks](https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0199004&type=printable)
**Published:** July 2018

**Data**

> Earthquake catalogs of these regions have been obtained from **United States Geological Survey** (USGS) [28] for the period from **January 1980 to December 2016**. These catalogs are initially evaluated for cut-off magnitude. Cut-off magnitude corresponds to the earthquake magnitude in the catalog above which catalog is complete and no seismic event is missing. This depends upon the level of instrumentation. Dense instrumentation in a region leads to better completeness of catalog with low cut-off magnitude. The cut-off magnitude for Southern California region is found to be less than 2.6, for Chile it is 3.4 and for Hindukush it is 4.0. The completeness of magnitude for all three regions shows the density of instrumentation in these regions. There are different methodologies proposed in literature for evaluation of cutoff magnitude [29]. In this study, cut-off magnitude is determined through Gutenberg-Richter
law. The point where curve deviates from exponential behavior is selected as a cut-off magnitude. All the events reported below cut-off magnitude are removed from the catalog before using for parameter calculation. Earthquake magnitudes and frequency of occurrences for each region is plotted as shown in Fig 1. The curves follow decreasing exponential behavior,
which assures that each catalog is complete to its respective cut-off magnitude

**Prediction**

Unclear, but my understanding is: each earthquake is labeled (1, 0) according to its magnitude being above +/- 5. Then 60 features were calculated based on the prior 50 seismic events in that region. The models attempt to predict whether a  a given earthquake is above 5 mag.

> In this study, earthquake prediction problem is designed/modeled as a binary classification problem. Every earthquake magnitude is converted to Yes, No (1, 0) through applying threshold on magnitude 5.0.

**Procedure**

>... separate training has been performed for each region. The reason
for separate training is that every region has different properties and can be classified tectonically into different categories, such as thrusting tectonics, strike-slip tectonics and so forth.
Therefore every type of region possess different behaviors and relations to the earthquakes.
Thus separate training for every region is meant to learn and model the relationship between
seismic features and earthquakes for that particular region

### [Earthquake magnitude prediction in Hindukush region using machine learning techniques](https://www.researchgate.net/publication/307951466_Earthquake_magnitude_prediction_in_Hindukush_region_using_machine_learning_techniques#)
**Date:** January 2017

**Data**
>There are two main sources of earthquake catalog for Hindukush region, Center forEarthquake Studies, which maintains an internal catalog of all the seismic events hap-pening in Pakistan along with the Hindukush and **United States Geological Survey** (Accessed on June, 2015). In Fig. 2, exponential rise in the occurrence of earthquakeswith decreasing magnitudes shows that it follows Gutenberg–Richter’s relationship, hencethe catalog is complete from magnitude 4.0 and onward. Therefore for mathematicalparameters calculation, **seismic events of magnitude greater than and equal to 4.0 areconsidered in this study.** There are a total of **11137 seismic events** recorded from **January, 1976 to December, 2013** and all of these are considered for this study. In this research, analysis is carried out on monthly basis and seismic parameters are calculated for every month on the basis of 100 seismic events before that month, as suggested by Panakkat and Adeli (2007).

**Prediction**
> The prediction task is treated as a binary classiﬁcation problem with earthquakes of magnitudes 5.5, and larger are considered as Yes or 1 and below as No or 0. After the training of these techniques, output is obtained on unseen data parameters, and then performance is evaluated in Sect. 6

**Procedure**: Authors only considered a single seismic region. They grouped the last 100 earthquakes prior to the start of each month, then engineered 8 features representing the characteristics of that group. The target was whether a 5.5+ event occured in the following month group or not. They trained various ML models and assessed each cell of the resultant contingency table.

### [An Evidence Based Earthquake Detector using Twitter](https://paperswithcode.com/paper/an-evidence-based-earthquake-detector-using)

### [Usage of multiple RTL features for Earthquakes prediction](https://arxiv.org/pdf/1905.10805v1.pdf)
**Date**: May 2019

**Data**: Japan, 1990-2016, 247, 204 earthquakes, magnitudes 5+

**Prediction**: will an earthquake with the magnitude above a 5.0  will take place at a 30-180 day horizon

### [Earthquakes magnitude prediction using recurrent neural networks](https://www.researchgate.net/publication/333671181_Earthquakes_magnitude_prediction_using_recurrent_neural_networks)
* **Date:** June 2019
* **Data:** Italian seismic catalog of earthquakes with magnitude equal or larger than 1.5 from 1995 to 2018

[ARTIFICIAL INTELLIGENCE BASED TECHNIQUES FOR EARTHQUAKE PREDICTION: A REVIEW](http://www.sci-int.com/pdf/8111108771495-1502--FAISAL%20AZAM--COMSAT--ISLAMABAD.pdf)

[Large Earthquake Magnitude Prediction in Chile with Imbalanced Classifiers and Ensemble Learning](https://pdfs.semanticscholar.org/105c/7a77a01eff4693db3a8b9c26f6650a076c41.pdf)

[Seismic activity prediction using computational intelligence techniques in northern Pakistan](https://www.researchgate.net/publication/320035816_Seismic_activity_prediction_using_computational_intelligence_techniques_in_northern_Pakistan)

### [Minimum Magnitude of Completeness in Earthquake Catalogs: Examples from Alaska, the Western United States, and Japan](ftp://seis.es.uwo.ca/pub/ktiampo/GR/Wiemer_MC.pdf)
> The first step toward understanding the characteristics of an earthquake catalog is to **discover the starting time of the high-quality catalog most suitable for analysis**. In addition, we seek to identify changes of reporting quality as a function of time. Issues connected with these problems are not the subjects of this article; they are dealt with elsewhere
(Habermann, 1986; Habermann, 1991; Zuniga and Wiemer, 1999; Zuniga and Wyss, 1995). **Here we assume that we know the starting date of the high-quality catalog**, and that there are no changes of reporting (magnitude stretches and shifts) serious enough to corrupt the analysis we have in mind, so that we may proceed to map Mc.

>The following steps are taken to estimate Mc: First we estimate the b- and a-value of the GR law as a function of minimum magnitude, based on the events with M  Mi. We use a maximum likelihood estimate to estimate the b- and a-values and their confidence limits (Aki, 1965; Shi and Bolt, 1982; Bender, 1983). Next, we compute a synthetic distribution of magnitudes with the same b-, a- and Mi values, which represents a perfect fit to a power law. To estimate the goodness of the fit we compute the absolute difference, R, of the number of events in each magnitude bin between the observed and synthetic distribution where Bi and Si are the observed and predicted cumulative number of events in each magnitude bin. We divide by the total number of observed events to normalize the distribution. Our approach is illustrated in Figure 2, which shows R as function of Mi. If Mi is smaller then the ‘correct’ Mc, the synthetic distribution based on a simple power law (squares in Figure 2) cannot model the FMD adequately and, consequently, the goodness of fit, measured in percent of the total number of events, is poor. The goodness-of-fit value R increases with increasing Mi and reaches a maximum value of
R 96% at Mc  1.8 in this example. At this Mc, a simple power law with the assumed b-, a-, and Mc value can explain
96% of the data variability. Beyond Mi  1.8, R increases again gradually. In this study we map Mc at the 90% level,
that is, we define Mc as the point at which a power law can model 90% or more of the FMD. For the example shown in
Figure 2, we therefore define Mc  1.5.

### [New Bayesian frequency-magnitude distribution model for earthquakes applied in Chile](https://www.researchgate.net/publication/325340620_New_Bayesian_frequency-magnitude_distribution_model_for_earthquakes_applied_in_Chile)

### ["Application of neural network and ANFIS model for earthquake occurrence in Iran"](https://www.researchgate.net/publication/263552794_Application_of_neural_network_and_ANFIS_model_for_earthquake_occurrence_in_Iran)

### No Access
[A probabilistic neural network for earthquake magnitude prediction](https://www.sciencedirect.com/science/article/pii/S0893608009000926?via%3Dihub)

[Neural networks to predict earthquakes in Chile](https://www.sciencedirect.com/science/article/pii/S1568494612004656)

"Earthquake prediction in seismogenic areas of the Iberian Peninsula" 

"Neural network models For earthquake magnitude prediction using multiple seismicity indicators" filetype:pdf

## Apps
### [App that crowdsources vibration data](https://myshake.berkeley.edu/)
