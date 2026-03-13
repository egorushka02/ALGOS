import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import heapq

st.set_page_config(page_title="Dijkstra's Algorithm Visualizer", layout="wide")

st.title("🔍 Dijkstra's Algorithm Visualizer")
st.markdown("Watch how Dijkstra's shortest path algorithm works step by step!")


def dijkstra(graph, start, end):
    """
    Dijkstra's algorithm with step-by-step tracking.
    Returns: distances, predecessors, steps
    """
    distances = {node: float('inf') for node in graph.nodes()}
    distances[start] = 0
    predecessors = {node: None for node in graph.nodes()}
    visited = set()
    steps = []
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
            
        visited.add(current_node)
        
        # Record step
        step_info = {
            'current': current_node,
            'visited': visited.copy(),
            'distances': distances.copy(),
            'predecessors': predecessors.copy(),
            'action': f"Processing node {current_node} (distance: {current_dist})"
        }
        steps.append(step_info)
        
        if current_node == end:
            break
        
        # Explore neighbors
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                weight = graph[current_node][neighbor]['weight']
                new_dist = current_dist + weight
                
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = current_node
                    heapq.heappush(pq, (new_dist, neighbor))
                    step_info['action'] += f"\n  → Updated {neighbor}: {new_dist}"
    
    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = predecessors[current]
    path.reverse()
    
    return distances, predecessors, steps, path if path[0] == start else []


def create_sample_graph():
    """Create a sample weighted graph for demonstration."""
    G = nx.Graph()
    
    # Add edges with weights
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'F', 6),
        ('E', 'F', 3),
    ]
    
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
    
    return G


# Sidebar controls
st.sidebar.header("⚙️ Controls")

# Graph selection
graph_type = st.sidebar.radio(
    "Graph Type",
    ["Sample Graph", "Custom Graph"]
)

if graph_type == "Sample Graph":
    G = create_sample_graph()
    nodes = list(G.nodes())
else:
    # Custom graph input
    st.sidebar.markdown("### Add Nodes")
    nodes_input = st.sidebar.text_input("Nodes (comma-separated)", "A, B, C, D, E")
    nodes = [n.strip() for n in nodes_input.split(',') if n.strip()]
    
    st.sidebar.markdown("### Add Edges")
    st.sidebar.markdown("Format: `node1, node2, weight`")
    default_edges = "\n".join([f"{nodes[i]}, {nodes[j]}, 1" for i in range(len(nodes)) for j in range(i+1, len(nodes))][:5])
    edges_input = st.sidebar.text_area("Edges (one per line)", value=default_edges, height=150)
    
    G = nx.Graph()
    G.add_nodes_from(nodes)
    
    for line in edges_input.split('\n'):
        parts = line.strip().split(',')
        if len(parts) >= 3:
            try:
                u, v, w = parts[0].strip(), parts[1].strip(), float(parts[2].strip())
                if u in nodes and v in nodes:
                    G.add_edge(u, v, weight=w)
            except ValueError:
                pass

# Node selection
if nodes:
    col1, col2 = st.columns(2)
    with col1:
        start_node = st.selectbox("Start Node", nodes, index=0 if 'A' in nodes else 0)
    with col2:
        end_node = st.selectbox("End Node", nodes, index=len(nodes)-1 if nodes else 0)

# Animation speed
speed = st.sidebar.slider("Animation Speed (ms)", 500, 3000, 1500, 500)

# Run button
if st.sidebar.button("🚀 Run Dijkstra's Algorithm", type="primary"):
    if len(nodes) < 2:
        st.error("Please add at least 2 nodes to the graph.")
    elif start_node == end_node:
        st.error("Start and end nodes must be different.")
    elif not G.edges():
        st.error("Please add at least one edge to the graph.")
    else:
        distances, predecessors, steps, path = dijkstra(G, start_node, end_node)
        
        # Display results
        st.header("📊 Results")
        
        if path and path[0] == start_node:
            st.success(f"**Shortest Path:** {' → '.join(path)}")
            st.info(f"**Total Distance:** {distances[end_node]}")
        else:
            st.warning(f"No path found from {start_node} to {end_node}")
        
        # Visualization
        st.header("🎬 Algorithm Visualization")
        
        # Create placeholder for the graph
        graph_placeholder = st.empty()
        step_info_placeholder = st.empty()
        
        # Initialize session state for step tracking
        if 'current_step' not in st.session_state:
            st.session_state.current_step = 0
        
        # Step navigation
        col1, col2, col3 = st.columns([1, 2, 1])
        with col1:
            if st.button("⏮️ First"):
                st.session_state.current_step = 0
        with col2:
            if st.button("▶️ Play/Pause"):
                st.session_state.playing = not st.session_state.get('playing', False)
        with col3:
            if st.button("⏭️ Last"):
                st.session_state.current_step = len(steps) - 1
        
        step_slider = st.slider(
            "Step", 
            0, 
            max(0, len(steps) - 1), 
            st.session_state.current_step,
            key="step_slider"
        )
        
        st.session_state.current_step = step_slider
        
        # Auto-play
        if st.session_state.get('playing', False) and steps:
            st.session_state.current_step = (st.session_state.current_step + 1) % len(steps)
            st.rerun()
        
        # Display current step
        if steps:
            step = steps[step_slider]
            
            # Create the visualization
            fig, ax = plt.subplots(figsize=(12, 8))
            pos = nx.spring_layout(G, seed=42)
            
            # Color nodes based on visited status
            node_colors = []
            for node in G.nodes():
                if node in step['visited']:
                    if node == step['current']:
                        node_colors.append('#FF6B6B')  # Current node (red)
                    else:
                        node_colors.append('#4ECDC4')  # Visited (teal)
                else:
                    node_colors.append('#95A5A6')  # Unvisited (gray)
            
            # Draw edges
            edge_weights = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edges(G, pos, ax=ax, width=2, alpha=0.5)
            
            # Draw edge labels (weights)
            nx.draw_networkx_edge_labels(
                G, pos, edge_labels=edge_weights, 
                ax=ax, font_size=10, label_pos=0.3
            )
            
            # Draw nodes
            nx.draw_networkx_nodes(
                G, pos, node_color=node_colors, 
                node_size=800, ax=ax, edgecolors='black', linewidths=2
            )
            
            # Draw node labels
            nx.draw_networkx_labels(G, pos, ax=ax, font_size=14, font_weight='bold')
            
            # Highlight path if found and we're at the last step
            if path and path[0] == start_node and step_slider == len(steps) - 1:
                path_edges = list(zip(path[:-1], path[1:]))
                nx.draw_networkx_edges(
                    G, pos, edgelist=path_edges,
                    edge_color='#FF6B6B', width=4, ax=ax
                )
            
            ax.set_title(f"Step {step_slider + 1}/{len(steps)}: {step['action']}", fontsize=12, pad=20)
            ax.axis('off')
            plt.tight_layout()
            
            graph_placeholder.pyplot(fig)
            plt.close()
            
            # Display step information
            step_info_placeholder.markdown(f"""
            ### Step {step_slider + 1} Details
            - **Current Node:** {step['current']}
            - **Visited Nodes:** {', '.join(sorted(step['visited']))}
            - **Current Distances:** {step['distances']}
            """)
        
        # Final distances table
        st.header("📋 Final Distances from Start Node")
        st.table({
            'Node': list(distances.keys()),
            'Shortest Distance': [distances[node] for node in distances.keys()],
        })

# About section
with st.expander("ℹ️ About Dijkstra's Algorithm"):
    st.markdown("""
    **Dijkstra's Algorithm** finds the shortest path between nodes in a weighted graph.
    
    ### How it works:
    1. Start at the source node with distance 0
    2. Mark all other nodes as having infinite distance
    3. Visit the unvisited node with the smallest distance
    4. Update distances to all neighbors through this node
    5. Mark the node as visited
    6. Repeat until reaching the destination or all nodes are visited
    
    ### Key Properties:
    - Works with **non-negative** edge weights
    - Uses a **priority queue** for efficiency
    - Time complexity: O((V + E) log V) with a min-heap
    - Guarantees the **optimal shortest path**
    """)
