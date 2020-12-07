# Apple Product Launch Analysis (September - November, 2020)


![apple_event](./images/one-more-thing-november.jpg)

**Authors:** [Dorjey Sherpa](https://www.linkedin.com/in/dorjey-sherpa-45501814a/), [Brendan Ferris](https://www.linkedin.com/in/brendangferris/)

## Overview

Over the past three months, Apple has had three major product launches:

<table>
<tr>
<th>Event Name</th>
<th> What was announced. </th>
<th> Date/Link </th>
</tr>
<tr>

</td>
<td>
<ol>
<li> Time Flies.</li>
<li> Hi, Speed.</li>
<li> One More Thing.</li>
</ol>
</td>

</td>
<td>
<ol>
<li> Apple Watch, Apple Fitness+, Apple One, IPad</li>
<li> HomePod Mini, IPhone 12, IPhone 12 Pro</li>
<li> M1 Chip/Apple Silicon, macOS Big Sur, Macbook Air, Mac Mini, MacBook Pro</li>
</ol>
</td>

</td>
<td>
<ul>
<li> <a href=https://www.youtube.com/watch?v=b13xnFp_LJs&t=2353s>September 15,2020</a></li>
<li> <a href=https://www.youtube.com/watch?v=KR0g-1hnQPA>October 13,2020</a></li>
<li> <a href=https://www.youtube.com/watch?v=5AwdkGKmZ0I>November 10,2020</a></li>
</ul>

</td>

</td>
</tr>
</table> 

Our task was to analyze the sentiment of tweets surrounding these events, and report out findings.  

## Business Problem

After every major event, thousands of people turn to social media to talk about what they have witnessed. 2020 has been a major year for apple with three different launches for their best selling items. They redesigned the iPhone, made a significant change in the internal components for their laptops and iPads and updated the software. In light of these crucial changes, Apple has tasked us with classifying and analyzing twitter data over the past three product launch events. We have two main tasks. First, we must train a classification algorithm to tag tweet sentiment as either positive/negative/neutral. Then, we will analyze all of the twitter data (from September 1, 2020 to December 1, 2020) regarding the product launches and see what information can be gleaned.

## Data

Using [twint](https://github.com/twintproject/twint), we were able to gather all tweets over the three month period between September and December which included the following terms/phrases: *IPhone 12, Apple Silicon, M1 MacBook, New MacBook, IPhone 12 Pro, New Apple, New IPhone, Silicon.* After removing non-english Tweets and duplicate posts, we obtained a total of [985,657 observations and 14 features](https://drive.google.com/file/d/1Eg5JYtw_DtpUsX3sn_KQpSXVYQ8JyErt/view?usp=sharing). After data cleaning and feature engineering, we were left with 981,535 tweets with 24 main features. 

This wordcloud illustrates the frequent terms among the tweets we gathered:

![overall_wordcloud](./images/all_tweets_wordcloud.png) 

## Methods

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Bibendum ut tristique et egestas. Consequat semper viverra nam libero justo laoreet sit. Fringilla ut morbi tincidunt augue interdum velit euismod in. Molestie at elementum eu facilisis. Scelerisque felis imperdiet proin fermentum leo. Commodo ullamcorper a lacus vestibulum sed. Semper eget duis at tellus. Fermentum dui faucibus in ornare. Sit amet nulla facilisi morbi tempus iaculis urna.

## Results

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Bibendum ut tristique et egestas. Consequat semper viverra nam libero justo laoreet sit. Fringilla ut morbi tincidunt augue interdum velit euismod in. Molestie at elementum eu facilisis. Scelerisque felis imperdiet proin fermentum leo. Commodo ullamcorper a lacus vestibulum sed. Semper eget duis at tellus. Fermentum dui faucibus in ornare. Sit amet nulla facilisi morbi tempus iaculis urna.

![sentiment over time](./images/sentiment_over_time.png)

## Conclusions

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Bibendum ut tristique et egestas. Consequat semper viverra nam libero justo laoreet sit. Fringilla ut morbi tincidunt augue interdum velit euismod in. Molestie at elementum eu facilisis. Scelerisque felis imperdiet proin fermentum leo. Commodo ullamcorper a lacus vestibulum sed. Semper eget duis at tellus. Fermentum dui faucibus in ornare. Sit amet nulla facilisi morbi tempus iaculis urna.

## Next Steps

There are instances where people use negative language in a positive way when describing apple products. For example, the phrase *'Apple M1 kills intel chips speed'* may be classified by our model as negative, when in fact it is positive. We developed a [small script](./scripts/tagger.py) that can be used to quickly tag tweets as positive/negative/neutral. Custom tagged tweets be saved in a .csv in your project directory. 

## For More Information

See the full modeling/analysis notebooks [here](path/to/notebooks) or review our [presentation](path/to).

For additional information, contact [Dorjey Sherpa](mailto:dorjeys3@gmail.com) or [Brendan Ferris](mailto:brendanfrrs@gmail.com).

## Repository Structure

<pre>
Place file tree here.
</pre>