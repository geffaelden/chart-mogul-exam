#### Customer Message
>Hi ChartMogul team,
>
>Really love using your product for my donut subscription service. I succeeded uploading a bunch of data
>in the UI and am considering building an integration with my in-house system once I complete my
>evaluation.
>
>There are a few questions I need to resolve:
>1) I would like to add the sales person that closed a deal to a customer profile in ChartMogul so that I can
>filter by this value. Should I bring this in as an attribute or tag? Is there an automated way to do this or do
>I need to push this data in manually?
>
>2) Another issue I had is that I can’t wrap my head around how proration works in ChartMogul.
>Here is my scenario:
>- My customer is on a monthly plan called Pro plan that costs $60 which they paid for on November 1st at
>3:23 pm.
>- On November 10th at 8:30pm they are upgrading to an Enterprise plan that costs $100.>
>
>How do I compute the invoice amount so the MRR for the upgrade to Enterprise plan is computed
>properly? Do you have any documentation about this?
>Yours truly,
>
>Homer Simpson

#### Support Reply

>Hi Homer,
>
>I'm glad to hear that Chart Mogul is suiting your needs and I'm more than happy to help you with your questions.
>
>1. For that specific scenario, I would suggest implementing this as an attribute to simpler filtering and segmentation. You can read more about attributes here https://help.chartmogul.com/hc/en-us/articles/206120219-Customer-attributes. Depending on the system you use, we have a couple of different automated ways to intergrate your attribute. I would say the simplest would be using our Google Sheets integration as demonstrated here https://help.chartmogul.com/hc/en-us/articles/207251069.
>
>2. The full documentation of how Chart Mogul computes MRR for invoices with proration is found here https://dev.chartmogul.com/docs/how-mrr-is-calculated-from-prorated-invoices. Basically, we compute MRR based on the number of seconds for proration. In your case, to compute for the proper prorated amount, you will need to know the time to be considered for proration and therefore there will are 3 relevant items to look at:
>
>|Invoice Item|Start Date|End Date|Full Amount|Number of seconds (End-Start)|Prorate Amount
>|-|-|-|-|-|-
>|Pro Plan (Original Subscription)|11-01-2019 15:23:00|12-01-2019 15:23:00|$60|2592000|$60 (Full)
>|Pro Plan (For Crediting)|11-10-2019 20:30:00|12-01-2019 15:23:00|$60|796020|-$41.57 (Prorate Credit)
>|Enterpise Plan (New Plan)|11-10-2019 20:30:00|12-01-2019 15:23:00|$100|796020|$69.29 (Prorate Charge)
>
>The prorate amount is the ratio of the remaining time in the subscription period and original full time of the subscription multiplied by the full amount of the plan. 
>
>I hope this helps! Let me know if you have further questions.
>
>All the best,
>Gef
