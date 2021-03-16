locals {
  origin_id = "my_origin"
}

resource "aws_cloudfront_distribution" "cdn" {
    origin {
        domain_name = aws_s3_bucket.bucket.website_endpoint
        origin_id   = local.origin_id
        custom_origin_config {
            http_port = 80
            https_port = 443
            origin_protocol_policy = "http-only"
            origin_ssl_protocols = ["TLSv1.2"]
        }
    }

    enabled             = true
    is_ipv6_enabled     = true
    default_root_object = "index.html"

    default_cache_behavior {
        allowed_methods  = ["HEAD", "GET"]
        cached_methods   = ["HEAD", "GET"]
        target_origin_id = local.origin_id
        viewer_protocol_policy = "redirect-to-https"

        # not really necessary for this basic S3 example
        forwarded_values {
            cookies {
                forward = "none"
            }
            query_string = false
        }
    }

    price_class = "PriceClass_200"

    restrictions {
        geo_restriction {
            restriction_type = "none"
        }
    }

    viewer_certificate {
        cloudfront_default_certificate = true
    }
}