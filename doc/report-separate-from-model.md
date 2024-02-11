Separate reports from models in Power BI Desktop
================================================



When creating a new Power BI Desktop solution, one of the first tasks you need to do is "get data". Getting data can result in two distinctly different outcomes. It could:


* Create a [live connection](../connect-data/desktop-report-lifecycle-datasets) to an already-published model, which could be either a Power BI semantic model ([previously known as a dataset](../connect-data/service-datasets-rename)) or a remote-hosted Analysis Services model.
* Commence the development of a new model, which could be either an Import, DirectQuery, or Composite model.


This article is concerned with the second scenario. It provides guidance on whether a report and model should be combined into a single Power BI Desktop file.


A *single file solution* works well when there's only ever a single report based on the model. In this case, it's likely that both the model and report are the efforts of the same person. We define it as a *Personal BI* solution, though the report could be shared with others. Such solutions can represent role-scoped reports or one-time assessments of a business challengeâoften described as *ad hoc* reports.



![A single file contains a model and report, developed by the same person.](media/report-separate-from-model/single-file-solution.png)




It makes sense to separate model and report development into separate Power BI Desktop files when:


* Data modelers and report authors are different people.
* It's understood that a model will be the source for multiple reports, now or in the future.



![There are three PBIX files. The first contains only a model. The other two contain only reports, and they live connect to the model hosted in the Power BI service. The reports are developed by different people.](media/report-separate-from-model/separate-report-files.png)




Data modelers can still use the Power BI Desktop report authoring experience to test and validate their model designs. However, just after publishing their file to the Power BI service they should remove the report from the workspace. And, they must remember to remove the report each time they republish and overwrite the semantic model.


Sometimes, model changes are inevitable. Data modelers must take care, then, not the break the model interface. If they do, it's possible that related report visuals or dashboard tiles will break. Broken visuals appear as errors, and they can result in frustration for report authors and consumers. And worseâthey can reduce trust in the data.


So, manage model changes carefully. If possible, avoid the following changes:


* Renaming tables, columns, hierarchies, hierarchy levels, or measures.
* Modifying column data types.
* Modifying measure expressions so they return a different data type.
* Moving measures to a different home table. It's because moving a measure could break report-scoped measures that fully qualify measures with their home table name. We don't recommend you write DAX expressions using fully qualified measures names. For more information, see [DAX: Column and measure references](/en-us/dax/best-practices/dax-column-measure-references).


Adding new tables, columns, hierarchies, hierarchy levels, or measures is safe, with one exception: It's possible that a new measure name could collide with a report-scoped measure name. To avoid collision, we recommend report authors adopt a naming convention when defining measures in their reports. They can prefix report-scoped measure names with an underscore or some other character(s).


If you must make breaking changes to your models, we recommend you either:


* [View related content for the semantic model](../consumer/end-user-related) in the Power BI service.
* Explore [Data lineage](../collaborate-share/service-data-lineage) view in the Power BI service.


Both options allow you to quickly identify any related reports and dashboards. Data lineage view is probably the better choice because it's easy to see the contact person for each related item. In fact, it's a hyperlink that opens an email message addressed to the contact.


We recommend you contact the owner of each related item to let them know of any planned breaking changes. This way, they can be prepared and ready to fix and republish their reports, helping to minimize downtime and frustration.


