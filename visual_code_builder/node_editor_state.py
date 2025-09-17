from enum import Enum

class NodeEditorState(Enum):
    """ Node editor state engine state"""

    """
    Represents the state where the node editor is in view mode. In this state,
    the user can interact with the nodes (viewing, moving or selecting) or
    interact with connections (selecting, creating or moving).
    """
    VIEW_MODE = 0

    """
    Represents the state where a connection is being dragged between nodes.
    In this state, the user is in the process of creating or modifying a
    connection between nodes.
    """
    CONNECTION_BEING_DRAGGED = 1