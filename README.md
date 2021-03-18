# Infrastructure
I implemented this by storing the html file in S3, then enabling website hosting on the S3 file. I then enabled a Cloudflare distribution to proxy that website. You can view this site at https://dlroh4hufir9l.cloudfront.net

Regarding testing, in the repo there is a `make test` target that simply curls the server. There are better ways of doing this of course, for example Terratest or Kitchen. You could even use something like Hashicorp's Sentinel to create Terraform policies like "all s3 objects must be private, except if the bucket is a website bucket". But for this assessment I kept the test simple.

Besides testing, some obvious ideas for improvement:

* Put a Route53 record alias on the Cloudfront
* Use your own certificate instead of the default Cloudfront one
* Use AWS WAF in front of Cloudfront. Some things you could enable would be the IP rules Amazon gives for free (contains IPs of common malware-infected hosts); block certain countries; rate limiting, etc. AWS WAF logs when any of these rules are triggered so you could build alarms around them.
* Restrict direct S3 access with Origin Access Identity (only allow files to be read through Cloudfront). In some cases, ensuring people only go through Cloudfront can be better for cost, not to mention security (all of the security we mentioned above would be useless if you could just go straight to S3).
* Set up origin failover so if the primary S3 origin is not working for whatever reason, requests are automatically served through a secondary origin instead.

All of the above ideas are for S3 websites. What if you don't have an S3 website, and you want to talk about a microservice of some kind?

* You may or may not want to use Cloudfront. It depends on whether you care if the extra complexity has the possibility of muddling things (to name one example, if you use Cloudformation you have to think about adding cache invalidation to your deployment jobs).
* Whether you use Cloudfront or just bare Load Balancers, you can still use WAF if you'd like to use the above use cases for WAF.
* Just like mentioned above for S3: you need to consider failover. For example, if you have two APIs running in different regions and a load balancer for each one, you can have a Route53 Failover-type record that will redirect requests to the secondary region when the first region is failing. You can also use Latency-type records to serve requests to your deployment geographically closest to the client.

# Coding
Assumes you're using Python 3.6. Tests are `make tests`, requires `pytest` from pip. It would be good practice to make a Dockerfile and a `requirements.txt` or a Poetry file of course, but didn't for something this simple.
