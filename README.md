# currency-watcher
Checks if the value of NOK is greater than the value of SEK. If true, it sends an email. 
The project is to be hosed in the cloud and run x number of times a day. 

If you wish to use the code to watch for different currency, you can change the currencies in "parameters" to the 3letter code, as well as the currency 
in "target = exchange["data"]["SEK"]["value"]" to the currency of your choice. 

I set the target to be greater than 1:1 to take account of the changing fee. 
