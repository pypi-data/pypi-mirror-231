# DP Serializers Client
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10-blue)](https://www.python.org/)


# Client package for DP Serializer

The dp-seriel-client enables serialization of popular Differential Privacy frameworks.
The client in dp-serializers-client makes it possible to serialize and query data with a corresponding server running.


## Creating Client:
```python
from fso_sdd_demo.client.client import Client
dp_client = Client("http://localhost:3031")
```
Once `fso_sdd_demo` is initialized it can be used to send requests to respective DP frameworks.

## Querying OpenDP
```python

pipeline = comb.make_pureDP_to_fixed_approxDP(
    trans.make_split_dataframe(separator=",", col_names=["col_1", "col_2", "col_3"]) >>
    trans.make_select_column(key="key_name", TOA=str) >>
    trans.make_cast(TIA=str, TOA=int) >>
    trans.make_impute_constant(0) >> 
    trans.make_clamp(bounds=(0, 1)) >>
    trans.make_bounded_sum((0, 1)) >>
    meas.make_base_discrete_laplace(scale=1.)
)

opendp_result = dp_client.opendp(pipeline)

#Data from API server with DP applied
print(opendp_result)
```


## Querying Smartnoise-SQL

```python
query_result = dp_client.sql(
    "SELECT col_1, COUNT(col_2) as ret_col_2 FROM comp.comp GROUP BY col_3", 1,0.0001
)

#Resulting data from APIs with DP applied
print(query_result)
```
