# Polygon API by Quantl
Implementation of polygon API by Quantl 
Polygon use swagger as our API spec and we used this swagger to generate most of the code that defines the REST client. This decision due to the size of our API, many endpoints and object definitions, and to accommodate future changes.

# Notes about Rest API
Every function call under our RESTClient has the query_params kwargs. These kwargs are passed along and mapped 1:1 as query parameters to the underling HTTP call. For more information on the different query parameters please reference Polygon API Docs.
