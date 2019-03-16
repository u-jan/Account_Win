### ReadMe 

You are a data scientist and you found this dataset of an organization called "X".

You want to analyze the dataset provided by an unknown company which did not declare the business case
or anything regarding their operations. This organization simply wants to hear about data.

As a well-rounded data scientist, you know the value add by telling stories about the data. 
Thus instead of creating a merely boring report, you decide to ask some meaningful questions which will create that story.

You are confident about only one aspect of the dataset; the target is a binary class called Won.

Won == 1 vs Won == 0

Your Thoughts:
 "Oh there are winners and others in this dataset. This is just like the real world. 
 I shall find who wins under what circumstances even thou I have absolutely no idea what they win."

And that's the case at least for the EDA part of the project:

### FIND WHO WINS OR WHAT MAKES WINNERS WIN

Secondly, you want to do more than mere EDA because you also want to demonstrate your machine learning skills. 
The problem is you don't want to intimidate them by being too techy to understand. 
You are already overkilling by adding this machine learning model to your project.
Yet business is for money and money speaks.
If you can generate a profit curve which finds the expected total profit in accordance with the model's performance.
You can continue to converse in business terms and this is another opportunity for you to declare your value add in terms of ROI.

Thereby for the second part of the project which is about machine learning, let's craft a scenario.
(I thought about going with something wild such as "these people are gladiators and won shows if they survive a battle where the amount is the bid") 
However, keeping it real and more humanitarian may offer benefits.  


**Crafted Scenario: You are a freelance data science consultant** (especially for cost-benefit-matrix I needed this small story)

The project in front of you is for a HR company which have junior and senior level account managers. 
These managers negotiate with managerial level candidates in order to convince them to accept positions provided by the customer companies.

For each successful hire, the HR company closes the deal as it generates revenue which is equivalent of "Amount" within the given data set.

In accordance with the compensation model of the company, senior recruiters have a higher rate of compensation compared to that of junior recruiters.
In addition, senior recruiters have higher chances of successfully closing a deal.

You ran your analysis and came up with the following proposal:

- Benefit from a binary classifier machine learning model which predicts if the deal ends up with success or failure.
- If a deal is predicted to be a success(Won == 1), assign junior recruiters for that deal so you generate more revenue.
- If a deal is predicted to be a failure(Won == 0), assign senior recruiters so they may change the course of current as they increase the chances of success with regard to their well-forged experience and network.
And if they fail to win the deal, you don't need to pay them because they failed.

**Result:** Cost decreases as revenue increases aka profit increases.

**ASSUMPTION:** The dataset is showing the historical deals of junior recruiters.

**Notes:**

The step_1 ipynb presents:
- EDA
- Feature Engineering
The step_2 ipynb presents:
- Modelling
- Model Improvement Notes
- ML oriented EDA
- Feature Engineering
- Cost Benefit Matrix
- Profit Curve
- Basic Model comparison


TO DO NEXT:
- Cross-Validation instead of a single train test split.
- ADD more models to see which one increases the performance the most
- GridSearch to find the best hyperparameters among models 
- Instead of a crafted senario, find out how you can increase performance of HR comapnies with similar strategies.


My special thanks to the professionals who provided me with the dataset.

                                                Jan


