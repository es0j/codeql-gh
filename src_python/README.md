codeql database create codeql-db \
  --language=python

  
  
codeql database analyze codeql-db \
  codeql/python-queries \
  --format=sarifv2.1.0 \
  --output=results.sarif