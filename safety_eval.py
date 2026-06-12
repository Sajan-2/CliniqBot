```python id="63kyl6"
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from datasets import Dataset

from rag_chain import build_chain


chain = build_chain()

# Sample test questions for evaluation
test_questions = [
    "What are symptoms of type 2 diabetes?",
    "What is hypertension and how is it treated?",
    "What does chest tightness indicate?"
]

# Run the chain and collect answers + contexts
data = {
    "question": [],
    "answer": [],
    "contexts": []
}

for q in test_questions:
    result = chain({"query": q})

    data["question"].append(q)
    data["answer"].append(result["result"])
    data["contexts"].append([result["result"]])

dataset = Dataset.from_dict(data)

scores = evaluate(
    dataset,
    metrics=[
        faithfulness,
        answer_relevancy
    ]
)

print(scores)
```
