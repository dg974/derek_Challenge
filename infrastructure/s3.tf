locals {
    html_files = ["index.html", "404.html"]
}

resource "aws_s3_bucket" "bucket" {
    bucket = "derek-gurchik-challenge"
    acl    = "private"

    website {
        index_document = "index.html"
        error_document = "404.html"
    }
}

resource "aws_s3_bucket_object" "index" {
    for_each = toset(local.html_files)
    bucket = aws_s3_bucket.bucket.id
    key    = each.key
    source = "files/${each.key}"
    acl    = "public-read"
    content_type = "text/html"
}