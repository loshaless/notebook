import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def plot_latency_charts(data):
    """
    Plot multiple line charts for latency analysis, one chart per interaction ID.
    
    Parameters:
    data (pandas.DataFrame): DataFrame with columns 'interaction_id', 'createdon', 'latency'
    """
    # Convert createdon to datetime if it's not already
    if not pd.api.types.is_datetime64_any_dtype(data['createdon']):
        data['createdon'] = pd.to_datetime(data['createdon'])
    
    # Get unique interaction IDs
    interaction_ids = data['interaction_id'].unique()
    
    # Calculate number of rows and columns for subplots
    n_charts = len(interaction_ids)
    n_cols = min(2, n_charts)  # Maximum 2 columns
    n_rows = (n_charts + n_cols - 1) // n_cols
    
    # Create figure with subplots
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5*n_rows))
    fig.suptitle('Latency Over Time by Interaction ID', fontsize=16, y=1.02)
    
    # Flatten axes array if multiple rows and columns
    if n_rows > 1 and n_cols > 1:
        axes = axes.flatten()
    elif n_rows == 1 and n_cols == 1:
        axes = [axes]
    elif n_rows == 1:
        axes = axes.flatten()
    
    # Create a line plot for each interaction ID
    for idx, interaction_id in enumerate(interaction_ids):
        interaction_data = data[data['interaction_id'] == interaction_id]
        
        # Sort by createdon
        interaction_data = interaction_data.sort_values('createdon')
        
        # Plot
        ax = axes[idx]
        ax.plot(interaction_data['createdon'], interaction_data['latency'], 
                marker='o', linestyle='-', linewidth=2, markersize=6)
        
        # Customize plot
        ax.set_title(f'Interaction ID: {interaction_id}')
        ax.set_xlabel('Created On')
        ax.set_ylabel('Latency (ms)')
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Rotate x-axis labels for better readability
        ax.tick_params(axis='x', rotation=45)
        
    # Remove empty subplots if any
    if n_charts < len(axes):
        for idx in range(n_charts, len(axes)):
            fig.delaxes(axes[idx])
    
    # Adjust layout to prevent overlapping
    plt.tight_layout()
    return fig

# Example usage:
if __name__ == "__main__":
    # Create sample data
    sample_data = {
        'interaction_id': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        'createdon': [
            '2024-01-01 10:00:00', '2024-01-01 11:00:00', '2024-01-01 12:00:00',
            '2024-01-01 10:00:00', '2024-01-01 11:00:00', '2024-01-01 12:00:00',
            '2024-01-01 10:00:00', '2024-01-01 11:00:00', '2024-01-01 12:00:00'
        ],
        'latency': [100, 150, 120, 200, 180, 220, 300, 280, 290]
    }
    
    df = pd.DataFrame(sample_data)
    
    # Create and show plots
    fig = plot_latency_charts(df)
    plt.show()
