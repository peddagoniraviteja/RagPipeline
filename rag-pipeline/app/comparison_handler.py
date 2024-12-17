import pandas as pd

def process_comparison_query(query, relevant_chunks):
    comparison_data = []  # Extract terms to compare from chunks
    for chunk in relevant_chunks:
        # Example: Custom extraction logic goes here
        comparison_data.append(parse_fields(chunk, query))  
    df = pd.DataFrame(comparison_data)
    return df.to_string(index=False)
