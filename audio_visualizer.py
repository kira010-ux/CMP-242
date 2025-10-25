# plugins/visualizer_plugin.py

import random
import time

class VisualizerPlugin:
    name = "Audio Visualizer"

    def on_load(self, player):
        self.player = player
        print(f"{self.name} initialized and ready.")

    def on_track_start(self, track):
        print(f"{self.name}: Starting visualization for '{track}'...")
        self.show_visuals()

    def on_track_stop(self, track):
        print(f"{self.name}: Visualization stopped for '{track}'.")

    def show_visuals(self):
        """Simulate live audio visualization."""
        for _ in range(3):
            level = random.randint(1, 10)
            #█ this represents the visualization bar
            print(f"🎶 {'█' * level}")
            time.sleep(0.5)
