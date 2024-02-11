Use SELECTEDVALUE instead of VALUES
===================================



As a data modeler, sometimes you might need to write a DAX expression that tests whether a column is filtered by a specific value.


In earlier versions of DAX, this requirement was safely achieved by using a pattern involving three DAX functions; [IF](../if-function-dax), [HASONEVALUE](../hasonevalue-function-dax) and [VALUES](../values-function-dax). The following measure definition presents an example. It calculates the sales tax amount, but only for sales made to Australian customers.



```
Australian Sales Tax =
IF(
    HASONEVALUE(Customer[Country-Region]),
    IF(
        VALUES(Customer[Country-Region]) = "Australia",
        [Sales] * 0.10
    )
)

```

In the example, the HASONEVALUE function returns TRUE only when a single value of the **Country-Region** column is visible in the current filter context. When it's TRUE, the VALUES function is compared to the literal text "Australia". When the VALUES function returns TRUE, the **Sales** measure is multiplied by 0.10 (representing 10%). If the HASONEVALUE function returns FALSEâbecause more than one value filters the columnâthe first IF function returns BLANK.


The use of the HASONEVALUE is a defensive technique. It's required because it's possible that multiple values filter the **Country-Region** column. In this case, the VALUES function returns a table of multiple rows. Comparing a table of multiple rows to a scalar value results in an error.


It's recommended that you use the [SELECTEDVALUE](../selectedvalue-function) function. It achieves the same outcome as the pattern described in this article, yet more efficiently and elegantly.


Using the SELECTEDVALUE function, the example measure definition is now rewritten.



```
Australian Sales Tax =
IF(
    SELECTEDVALUE(Customer[Country-Region]) = "Australia",
    [Sales] * 0.10
)

```


Tip


It's possible to pass an *alternate result* value into the SELECTEDVALUE function. The alternate result value is returned when either no filtersâor multiple filtersâare applied to the column.



