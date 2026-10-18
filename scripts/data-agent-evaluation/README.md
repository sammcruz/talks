# Data agent evaluation

Companion notebooks for the talks on Fabric data agents. They show how to **test a data agent with your own ground truth** instead of trusting it blindly.

| Language | Notebook |
|---|---|
| English | [`data_agent_evaluation_en.ipynb`](data_agent_evaluation_en.ipynb) |
| Español | [`data_agent_evaluation_es.ipynb`](data_agent_evaluation_es.ipynb) |

Both notebooks do the same four things, with comments and explanations in each language:

1. Compute eight business answers with plain Spark SQL, so the expected answers come from the data.
2. Assemble a `question` / `expected_answer` table.
3. Run the evaluation with the Fabric Data Agent SDK, using a custom critic prompt so the check is about correctness, not formatting.
4. Read the summary and the step-by-step details.

## What you need

- A Fabric workspace with a published Data Agent connected to the Olist tables.
- The public [Olist Brazilian E-Commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) loaded as Delta tables in a Lakehouse (check the dataset page for its license; the data is not included here).
- The notebook opened in that workspace with the Lakehouse as its default.
- Set `data_agent_name` in step 3 to your agent's name.

## Notes

- Outputs were removed on purpose, so the notebooks carry no workspace names, ids or run history.
- The critic prompt is in English in both versions. You can translate it, but re-test the result.
- Documentation: [Evaluate your data agent](https://learn.microsoft.com/en-us/fabric/data-science/evaluate-data-agent).

Used in: Data Saturday Sofia 2026, Queensland Power BI and Fabric User Group (English); Power BI & Fabric Barcelona, January 2026 (Spanish). See the [talks list](../../README.md).
