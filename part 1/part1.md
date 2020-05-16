## Part 1

#### Create Custom Data Source
Custom data source was created with the following details
>Name: Test Data Source
<br>DS UUID: ds_8533523b-9680-11ea-9f4e-9302c2ed3851 (system generated)

#### Create 10 Customers 
10 customers were arbitrarily defined with name and external id provided. The uuid was system generated upon creation.

| name  | external_id | uuid 
| - | - | - 
| Leslie Knope | 1 | cus_42a41ffc-9681-11ea-9ff1-db5c3fa181ad 
| Ann Perkins | 2 | cus_9bba3232-9681-11ea-a02f-2b59be799449 
| Mark Brendanawicz | 3 | cus_9ef4865c-9681-11ea-a02f-d3a870d57ca9 
| Tom Haverford | 4 | cus_a31738ae-9681-11ea-a031-cbc36e5f2736 
| Ron Swanson | 5 | cus_a51f12c0-9681-11ea-a031-2f896fa15afd 
| April Ludgate | 6 | cus_a75a3b7c-9681-11ea-a031-bface765eaae 
| Andy Dwyer | 7 | cus_aa614459-9681-11ea-a032-6b22b5b9116f 
| Ben Wyatt | 8 | cus_ad602822-9681-11ea-a034-5badada252bc 
| Chris Traeger | 9 | cus_af415629-9681-11ea-a035-b37853ce3109 
| Jerry Gergich | 10 | cus_b22165f5-9681-11ea-a038-a32a87358011 

#### Create 3 Plans
3 Plans were created based on the instruction. Price documented for invoicing purposes

| name  | term | plan_id | price 
| - | - | - | - 
| Silver | monthly | silver-montly | 49 usd
| Gold | monthly | gold-montly | 149 usd
| Diamond | annual | diamond-annual | 1499 usd

#### Subscription, Invoices, and Invoice Items

| name  | plan id | status | start date | invoice
| - | - | - | - | -
| Chris Traeger | diam_00001 | active | 01/07/2020 | parks_01003_09
| Ron Swanson | diam_00002 | cancelled | 02/09/2020 | parks_02007_05
| Tom Haverford | diam_00003 | active | 04/25/2020 | parks_04008_04
| Leslie Knope | gold_00001 | active | 01/05/2020 | parks_01001_01
|  |  |  |  | parks_02001_01
|  |  |  |  | parks_03001_01
|  |  |  |  | parks_04001_01
| Andy Dwyer | gold_00002 | cancelled | 03/05/2020 | parks_03005_07
|  |  |  |  | parks_04005_07
| Ben Wyatt | gold_00003 | cancelled | 03/02/2020 | parks_02004_08
| Jerry Gergich | gold_00004 | active | 04/21/2020 | parks_04002_10
| Ben Wyatt | gold_00005 | active | 02/02/2020 | parks_03004_08
|  |  |  |  | parks_04004_08
| Ann Perkins | silv_00001 | active | 03/06/2020 | parks_03010_02
|  |  |  |  | parks_04010_02
| Mark Brendanawicz | silv_00002 | active | 01/19/2020 | parks_01009_03
|  |  |  |  | parks_02009_03
|  |  |  |  | parks_03009_03
|  |  |  |  | parks_04009_03
| April Ludgate | silv_00003 | cancelled | 04/13/2020 | parks_04006_06

#### Full refund
Add full refunds to 2 customers

| invoice  | refund id | refund date 
| - | - | - 
| parks_04006_06 (April Ludgate) | refund_2020040001 | 2020-04-22 
| parks_02004_08 (Ben Wyatt) | refund_2020020002 | 2020-02-07 

#### One Time Charge
Add one time charges to 3 customers

| invoice  | amount | description
| - | - | - 
| parks_01003_09 (Chris Traeger) | $499.00 | 99.99% Service Guarantee
| parks_04008_04 (Tom Haverford) | $150.00 | Premium Features
| parks_04005_07 (Andy Dwyer) | $10.00 | Late Payment Fee

#### Cancellations
Add cancellations to 4 customers

| name  | sub_id | cancel date
| - | - | - 
| Ron Swanson | diam_00002 | 2020-04-29
| Andy Dwyer | gold_00002 | 2020-04-30
| Ben Wyatt | gold_00003 | 2020-02-07
| April Ludgate | silv_00003 | 2020-04-22
