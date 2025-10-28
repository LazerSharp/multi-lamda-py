# Use bash for scripting
set shell := ["bash", "-cu"]

# === CONFIGURATION ===
project := "sam-uv-app-v4"
region := "us-east-1"
s3_bucket := "plabs-deploy-artifacts-t0"
stack_name := "sam-uv-stack-v4"
template := "template.yaml"
build_dir := ".aws-sam/build"

# === COMMANDS ===

# Print current AWS region
aws-region:
	aws configure get region

# Sync all deps using uv (ensures reproducibility)
deps:
	@echo "🔁 Syncing uv workspace dependencies..."
	uv sync --frozen

# Run all unit tests (layers + functions)
test:
	@echo "🧪 Running tests..."
	uv run pytest  functions/order_service/
	uv run pytest  functions/order_service/
	uv run pytest  layers/common/
	uv run pytest  layers/thirdparty/


# Build layers and functions using uv
build:
	#!/usr/bin/env bash
	@echo "📦 Building all layers and Lambdas..."
	uv sync --frozen
	rm -rf {{build_dir}}
	mkdir -p {{build_dir}}

	# Build Common Layer
	uv build --package commonlib
	mkdir -p {{build_dir}}/common_layer/python/
	cp -r layers/common/src/commonlib {{build_dir}}/common_layer/python/

	# Build Thirdparty Layer
	uv build --package thirdparty
	mkdir -p {{build_dir}}/thirdparty_layer/python
	# uv pip install --no-cache-dir  --target {{build_dir}}/thirdparty_layer/python

	uv export --format requirements-txt --no-hashes --output-file {{build_dir}}/thirdparty_layer/requirements.txt --package thirdparty > /dev/null
	
	# Install to build directory with Lambda-compatible wheels
	uv pip install --python-platform x86_64-manylinux2014 --only-binary=:all: \
		--python-version 3.9 --target {{build_dir}}/thirdparty_layer/python \
		-r {{build_dir}}/thirdparty_layer/requirements.txt

	# Package Functions
	for fn in functions/*; do \
		name=$(basename $fn); \
		echo "📦 Building function: $name"; \
		mkdir -p {{build_dir}}/$name/; \
		cp -r $fn/src/* {{build_dir}}/$name/; \
	done

# SAM Package (requires pre-created S3 bucket)
package:
	@echo "📤 Packaging SAM..."
	sam package \
	  --template-file {{template}} \
	  --output-template-file packaged.yaml \
	  --s3-bucket {{s3_bucket}}

# Deploy to AWS
deploy:
	@echo "🚀 Deploying SAM Stack..."
	sam deploy \
	  --template-file packaged.yaml \
	  --stack-name {{stack_name}} \
	  --capabilities CAPABILITY_IAM \
	  --region {{region}}

# Clean up build artifacts
clean:
	rm -rf {{build_dir}} .uv __pycache__ */__pycache__ */*/__pycache__
	@echo "🧹 Clean complete!"

# Shortcut: end-to-end build + test + deploy
release: clean deps test build package deploy

