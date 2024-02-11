Relationship troubleshooting guidance
=====================================



This article targets you as a data modeler working with Power BI Desktop. It provides guidance on how to troubleshoot specific issues that you might encounter when developing models and reports.



Note


An introduction to model relationships is not covered in this article. If you're not completely familiar with relationships, their properties or how to configure them, we recommend that you first read the [Model relationships in Power BI Desktop](../transform-model/desktop-relationships-understand) article.


It's also important that you have an understanding of star schema design. For more information, see [Understand star schema and the importance for Power BI](star-schema).



When a report visual is set up to use fields from two (or more) tables, and it doesn't present the correct result (or any result), it's possible that the issue is related to model relationships.


In this case, here's a general troubleshooting checklist to follow. You can progressively work through the checklist until you identify the issue(s).


1. Switch the visual to a table or matrix, or open the *See Data* paneâit's easier to troubleshoot issues when you can see the query result.
2. If there's an empty query result, switch to Data viewâverify that tables have been loaded with rows of data.
3. Switch to Model viewâit's easy to see the relationships and quickly determine their properties.
4. Verify that relationships exist between the tables.
5. Verify that cardinality properties are correctly setâthey could be incorrect if a "many"-side column presently contains unique values, and it has been incorrectly set as a "one" side.
6. Verify that the relationships are active (solid line).
7. Verify that the filter directions support propagation (interpret arrow heads).
8. Verify that the correct columns are relatedâeither select the relationship, or hover the cursor over it to reveal the related columns.
9. Verify that the related column data types are the same, or at least compatibleâit's possible to relate a text column to a whole number column, but filters won't find any matches to propagate filters.
10. Switch to Data view, and verify that matching values can be found in related columns.


Here's a list of issues and their possible reasons.




| **Issue** | **Possible reason(s)** |
| --- | --- |
| The visual displays no result | â¢Â The model is yet to be loaded with data. â¢Â No data exists within the filter context. â¢Â Row-level security (RLS) is enforced. â¢Â Relationships aren't propagating between tablesâ*follow checklist above*. â¢Â RLS is enforced, but a bi-directional relationship isn't enabled to propagateâsee [Row-level security (RLS) with Power BI Desktop](/en-us/power-bi/enterprise/service-admin-rls). |
| The visual displays the same value for each grouping | â¢Â Relationships don't exist. â¢Â Relationships aren't propagating between tablesâ*follow checklist above*. |
| The visual displays results, but they aren't correct | â¢Â Visual is incorrectly set up. â¢Â Measure calculation logic is incorrect. â¢Â Model data needs to be refreshed. â¢Â Source data is incorrect. â¢Â Relationship columns are incorrectly related (for example, **ProductID** column maps to **CustomerID**). â¢Â It's a relationship between two DirectQuery tables, and the "one"-side column of a relationship contains duplicate values. |
| BLANK groupings or slicer/filter items appear, and the source columns don't contain BLANKs | â¢Â It's a regular relationship, and "many"-side column contain values not stored in the "one"-side columnâsee [Model relationships in Power BI Desktop (Regular relationships)](/en-us/power-bi/transform-model/desktop-relationships-understand#regular-relationships). â¢Â It's a regular one-to-one relationship, and related columns contain BLANKsâsee [Model relationships in Power BI Desktop (Regular relationships)](/en-us/power-bi/transform-model/desktop-relationships-understand#regular-relationships). â¢Â An inactive relationship "many"-side column stores BLANKs, or has values not stored on the "one" side. |
| The visual is missing data | â¢Â Incorrect/unexpected filters are applied. â¢Â RLS is enforced. â¢Â It's a limited relationship, and there are BLANKs in related columns, or data integrity issuesâsee [Model relationships in Power BI Desktop (limited relationships)](/en-us/power-bi/transform-model/desktop-relationships-understand#limited-relationships). â¢Â It's a relationship between two DirectQuery tables, the relationship is set to [assume referential integrity](/en-us/power-bi/transform-model/desktop-relationships-understand#assume-referential-integrity), but there are data integrity issues (mismatched values in related columns). |
| RLS isn't correctly enforced | â¢Â Relationships aren't propagating between tablesâ*follow checklist above*. â¢Â RLS is enforced, but a bi-directional relationship isn't enabled to propagateâsee [Row-level security (RLS) with Power BI Desktop](/en-us/power-bi/enterprise/service-admin-rls). |


