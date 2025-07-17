"""
Defines the path of each icons in the UI
"""

from pathlib import Path
ui_path = Path(__file__).parent
icons_path = ui_path / 'icons'

#* Parent window icons paths
parent_icon = [ icons_path / 'add.svg', 
                icons_path / 'play_arrow.svg',
                icons_path / 'settings.svg',
                icons_path / 'search.svg' ]
