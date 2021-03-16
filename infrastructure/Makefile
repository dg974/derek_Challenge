ENV?=dev

.PHONY: init plan apply test

init:
	terraform init

plan:
	terraform plan -out plans/${ENV}.plan

apply:
	terraform apply plans/${ENV}.plan

test:
	curl -s https://dlroh4hufir9l.cloudfront.net | grep "SecNet" > /dev/null