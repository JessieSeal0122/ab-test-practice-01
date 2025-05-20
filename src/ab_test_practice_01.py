import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time

# === 0. Start timer ===
start_time = time.time()

# === 1. Data folder path ===
DATA_DIR = r"C:\Users\Python\ab_test_project\data"  # ← Adjust this path

# === 2. Read and clean column names ===
def load_and_clean(filepath, group_label):
    df = pd.read_csv(filepath, sep=';')
    df['Campaign Group'] = group_label
    df.columns = (
        df.columns
        .str.replace('#', '', regex=False)
        .str.replace('[', '', regex=False)
        .str.replace(']', '', regex=False)
        .str.replace(' ', '_')
        .str.strip()
    )
    return df

control_df = load_and_clean(os.path.join(DATA_DIR, "control_group.csv"), "Control")
test_df = load_and_clean(os.path.join(DATA_DIR, "test_group.csv"), "Test")
df = pd.concat([control_df, test_df], ignore_index=True)

# === 3. Calculate conversion metrics ===
df['CTR'] = df['_of_Website_Clicks'] / df['_of_Impressions']
df['Add_to_Cart_Rate'] = df['_of_Add_to_Cart'] / df['_of_View_Content']
df['Purchase_Rate'] = df['_of_Purchase'] / df['_of_Add_to_Cart']

# === 4. t-test function ===
def run_t_test(df, metric):
    group1 = df[df['Campaign_Group'] == 'Control'][metric].dropna()
    group2 = df[df['Campaign_Group'] == 'Test'][metric].dropna()
    t_stat, p_value = stats.ttest_ind(group1, group2)
    return {
        'Metric': metric,
        'Control Mean': group1.mean(),
        'Test Mean': group2.mean(),
        'T-Statistic': t_stat,
        'P-Value': p_value
    }

# === 5. Perform t-tests on all metrics ===
metrics = ['CTR', 'Add_to_Cart_Rate', 'Purchase_Rate']
results = [run_t_test(df, m) for m in metrics]
summary_df = pd.DataFrame(results)
print("\n📊 A/B Test T-Test Summary:")
print(summary_df.round(4))

# === 6. Plot grouped bar chart ===
step_start = time.time()
melted = df.melt(id_vars='Campaign_Group', value_vars=metrics,
                 var_name='Metric', value_name='Rate')
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=melted, x='Metric', y='Rate', hue='Campaign_Group', errorbar='sd', ax=ax)
ax.set_title("Conversion Rate Comparison (CTR / Add-to-Cart / Purchase)")
ax.set_ylabel("Rate")
ax.set_ylim(0, 1)
ax.grid(True)
fig.tight_layout()

# Save chart
barplot_path = os.path.join(DATA_DIR, "..", "conversion_rate_comparison_all.png")
fig.savefig(barplot_path, bbox_inches='tight')
plt.close(fig)
print(f"📁 Chart saved to: {os.path.abspath(barplot_path)}")
print(f"✅ Chart saved in {time.time() - step_start:.2f} seconds")

# === 7. Write log file ===
step_start = time.time()
log_path = os.path.join(DATA_DIR, "..", "ab_test_run_log.txt")
with open(log_path, 'w', encoding='utf-8') as f:
    f.write("📄 A/B Test Execution Log\n")
    f.write("="*40 + "\n")
    f.write(f"🕒 Run Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write(f"⏱️ Elapsed Time: {time.time() - start_time:.2f} seconds\n\n")
    f.write("📊 T-Test Results:\n")
    f.write(summary_df.round(4).to_string(index=False))
    f.write("\n\n📁 Chart saved at:\n")
    f.write(os.path.abspath(barplot_path) + "\n")
    f.write("\n✅ Analysis completed successfully.\n")
print(f"📝 Log saved to: {os.path.abspath(log_path)}")
print(f"✅ Log completed in {time.time() - step_start:.2f} seconds")

# === 8. Output summary_df as table image ===
step_start = time.time()
fig, ax = plt.subplots(figsize=(8, 2))
ax.set_axis_off()
table = ax.table(
    cellText=summary_df.round(4).values,
    colLabels=summary_df.columns,
    cellLoc='center',
    loc='center'
)
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.5)
summary_img_path = os.path.join(DATA_DIR, "..", "ab_test_summary_table.png")
fig.tight_layout()
fig.canvas.draw()
fig.savefig(summary_img_path, bbox_inches='tight')
plt.close(fig)
print(f"🖼️ Summary table image saved to: {os.path.abspath(summary_img_path)}")
print(f"✅ Table image generated in {time.time() - step_start:.2f} seconds")

# === 9. Final message ===
elapsed = time.time() - start_time
print(f"\n⏱️ Total execution time: {elapsed:.2f} seconds")
print("🎉 A/B test analysis completed successfully!")

# === 10. End of script ===
