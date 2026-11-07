
# This creates the page for displaying data visualizations.

import streamlit as st
import json
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Volleyball Statistics",
    page_icon="🏐"
)

# PAGE TITLE
st.title("🏐 Volleyball Player Statistics")
st.write("2026 Volleyball Nations League")
st.write("Compare professional volleyball players and their statistics!")

# PART 1: GRAPHS FROM data.json

file_path = Path(__file__).resolve().parent.parent / "data.json"

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

players = data["data_points"]

df = pd.DataFrame(players)

# GRAPH 1: STATIC BAR CHART

st.header("Total Points by Player")

st.write("This graph compares the total points scored by each player.")

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(df["name"], df["total_points"], color="royalblue")

ax.set_title("Total Points Scored")
ax.set_xlabel("Volleyball Players")
ax.set_ylabel("Total Points")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig)

# GRAPH 2: DYNAMIC SCATTER PLOT

st.header("Interactive Player Statistics")

st.write("Choose a statistic to compare the players.")


if "selected_stat" not in st.session_state:
    st.session_state.selected_stat = "kills"


stat = st.selectbox(
    "Select a statistic:",
    ["kills", "blocks", "aces", "total_points"],
    key="selected_stat"
)


fig2, ax2 = plt.subplots(figsize=(10, 6))

ax2.scatter(
    df["name"],
    df[stat],
    color="orange",
    s=100
)

ax2.set_title("Player Comparison: " + stat.title())
ax2.set_xlabel("Volleyball Players")
ax2.set_ylabel(stat.replace("_", " ").title())

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig2)


# GRAPH 3: INTERACTIVE PIE CHART

st.header("Player Scoring Breakdown")
st.write("Select a player to see how they scored their points.")

if "selected_player" not in st.session_state:
    st.session_state.selected_player = df["name"].iloc[0]

selected_player = st.selectbox(
    "Choose a player:",
    df["name"].tolist(),
    key="selected_player"
)

player_data = df[df["name"] == selected_player].iloc[0]

categories = ["Kills", "Blocks", "Aces"]
values = [
    player_data["kills"],
    player_data["blocks"],
    player_data["aces"]
]

fig3, ax3 = plt.subplots()

ax3.pie(
    values,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90
)

ax3.set_title(selected_player + " - Scoring Breakdown")

st.pyplot(fig3)





# Choose from all players in data.json


from urllib.parse import quote_plus

st.header("🏐 Player Highlights")

player = st.selectbox(
    "Choose a player:",
    df["name"].tolist()
)

search = player + " volleyball highlights"

url = (
    "https://www.youtube.com/results?search_query="
    + quote_plus(search)
)

st.link_button("Watch Highlights on YouTube", url)





# PART 2: GRAPHS FROM data.csv

st.divider()

st.title("📊 Data From the Fan Survey")

st.write("These graphs use votes collected from visitors on the Survey page.")

st.info("Want to participate? Visit the Survey page and vote for your favorite volleyball player!")

st.header("🏐 Most Popular Volleyball Players")
st.write("This graph shows how many fan votes each player has received.")

csv_path = Path(__file__).resolve().parent.parent / "data.csv"

if csv_path.exists() and csv_path.stat().st_size > 0:

    votes_df = pd.read_csv(csv_path)

    if not votes_df.empty:
        vote_counts = votes_df["Category"].value_counts()

        fig4, ax4 = plt.subplots(figsize=(10, 6))

        ax4.bar(vote_counts.index, vote_counts.values, color="skyblue")

        ax4.set_title("Most Popular Volleyball Players")
        ax4.set_xlabel("Volleyball Players")
        ax4.set_ylabel("Number of Fan Votes")

        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()

        st.pyplot(fig4)

    else:
        st.info("No fan votes have been submitted yet.")

else:
    st.info("No fan votes have been submitted yet.")

# GRAPH 5: WHY FANS LOVE THEIR FAVORITE PLAYERS

st.header("🏐 Why Fans Love Their Favorite Players")

st.write("Choose a player to see why fans voted for them.")

if csv_path.exists() and csv_path.stat().st_size > 0:

    votes_df = pd.read_csv(csv_path)

    if not votes_df.empty:

        # Remember which player the user selects
        if "fan_player" not in st.session_state:
            st.session_state.fan_player = "All Players"

        player_options = ["All Players"] + sorted(
            votes_df["Category"].dropna().unique().tolist()
        )

        selected_player = st.selectbox(
            "Select a player:",
            player_options,
            key="fan_player"
        )

        # Filter the survey responses
        if selected_player == "All Players":
            filtered_votes = votes_df
        else:
            filtered_votes = votes_df[
                votes_df["Category"] == selected_player
            ]

        # Count the reasons fans selected
        reason_counts = filtered_votes["Value"].value_counts()

        if not reason_counts.empty:

            fig5, ax5 = plt.subplots(figsize=(7, 7))

            ax5.pie(
                reason_counts.values,
                labels=reason_counts.index,
                autopct="%1.1f%%",
                startangle=90
            )

            ax5.set_title("Reasons Fans Choose Their Favorite Players")

            st.pyplot(fig5)

        else:
            st.info("No votes available for this player.")

    else:
        st.info("No survey responses yet.")

else:
    st.info("No survey responses yet.")



