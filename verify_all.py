"""References:
https://wellformedness.com/courses/LING83800/
https://github.com/kylebgorman/Pynini/issues/6
"""

from fst_generate import Adjective
import pynini as pn
from pynini.lib.rewrite import matches as pn_matches
import pandas as pd

# Load the adjectives
df_adj_forme = pd.read_csv("adjective_forme.csv")

# Get the unique adjectives
unique_adjectives = df_adj_forme["base_form"].unique().tolist()
num_adj = len(unique_adjectives)

# For each unique adjective, check its forms
good_adjectives = 0
corrupt = 0
for adj in unique_adjectives:
    try:
        adj = adj.strip()

        # Generate forms
        adj_obj = Adjective(adj)
        adj_obj.generate_all_forms()

        # Get the gold forms
        gold_forms = df_adj_forme[df_adj_forme["base_form"] == adj]

        # Compare
        assert pn_matches(
            adj,
            gold_forms[
                (gold_forms["gender"].str.contains("masculin"))
                & (gold_forms["number"].str.contains("singular"))
            ]["inflection"]
            .iloc[0]
            .strip(),
            adj_obj.generated_forms[0],
            input_token_type="utf8",
            output_token_type="utf8",
        )

        assert pn_matches(
            adj,
            gold_forms[
                (gold_forms["gender"].str.contains("feminin"))
                & (gold_forms["number"].str.contains("singular"))
            ]["inflection"]
            .iloc[0]
            .strip(),
            adj_obj.generated_forms[1],
            input_token_type="utf8",
            output_token_type="utf8",
        )

        assert pn_matches(
            adj,
            gold_forms[
                (gold_forms["gender"].str.contains("masculin"))
                & (gold_forms["number"].str.contains("plural"))
            ]["inflection"]
            .iloc[0]
            .strip(),
            adj_obj.generated_forms[2],
            input_token_type="utf8",
            output_token_type="utf8",
        )

        assert pn_matches(
            adj,
            gold_forms[
                (gold_forms["gender"].str.contains("feminin"))
                & (gold_forms["number"].str.contains("plural"))
            ]["inflection"]
            .iloc[0]
            .strip(),
            adj_obj.generated_forms[3],
            input_token_type="utf8",
            output_token_type="utf8",
        )

        good_adjectives += 1
    except Exception as e:
        if type(e) == pn.lib.rewrite.Error:
            corrupt += 1


print(f"Good: {good_adjectives}")
print(f"Corrupt: {corrupt}")
print(f"Total: {num_adj}")

print(f"Covered: {good_adjectives / (num_adj - corrupt) * 100:.2f}%")
