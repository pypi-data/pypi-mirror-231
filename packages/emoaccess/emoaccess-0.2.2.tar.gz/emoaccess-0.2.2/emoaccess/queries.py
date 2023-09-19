import pandas as pd
import numpy as np
from typing import Optional, List


def _yesterday():
    pass


def get_annotation_ids_for_acquisition_id(acquisition_id: str = None,
                                          conn=None):

    """
    Gets the annotation ids for an acquisition id.

    Args:
        acquisition_id: acquisition id
        conn: database connection

    Returns:
        annotation ids
    """
    pass


def get_cell_coordinates_for_acquisition_id(acquisition_id: str = None,
                                            segmentation_version: int = None,
                                            conn=None) -> pd.DataFrame:

    """
    Gets the cell coordinates for an acquisition id.

    Args:
        acquisition_id: acquisition id
        segmentation_version: segmentation version
        conn: database connection

    Returns:
        cell coordinates
    """
    pass


def get_story_id_from_study_id_and_title(study_id, story_title, conn):
    """
    Given a study_id and story_title, return the story_id.

    Args:
        study_id: int representing unique study id.
        story_title: string representing (hopefully) unique story title.
        conn: database connection

    Returns:
        story_id: int representing unique story id.
    """
    pass


def get_note_title_from_note_id(note_id, conn):
    """
    Given a note_id, return the note_title.

    Args:
        note_id: int representing unique note id.
        conn: database connection

    Returns:
        note_title: string representing unique note title.
    """
    pass


def get_all_masks_for_story(study_id, story_title, conn):
    pass


def get_segmentation_masks_for_acquisition_id(acquisition_id: str = None,
                                              study_id: Optional[int] = None,
                                              seg_version: int = None
                                              ) -> np.ndarray:

    """
    Returns the segmentation mask for a given acquisition_id.

    Args:
        acquisition_id: str representing unique acquisition id.
        study_id: int representing unique study id.

    Returns:
        A numpy array of the segmentation mask.
    """
    pass


def get_story_ids_for_acquisition_id(acquisition_id: str = None,
                                     conn=None) -> List[int]:

    """
    Returns the story ids for a given acquisition_id.
    """
    pass


def get_all_note_ids_for_acquisition_id(acquisition_id: str = None,
                                        conn=None) -> List[int]:

    """
    Returns the note ids for a given acquisition_id.
    """
    pass


def get_roi_df_for_acquisition_id(acquisition_id: str = None,
                                  conn=None) -> pd.DataFrame:
    pass


def get_cell_anno_df(acquisition_id: str = None) -> pd.DataFrame:
    pass


def get_biomarker_and_segmentation_versions_for_study_acquisitions(study_id: int = None,
                                                                   conn=None) -> pd.DataFrame:
    pass


def get_all_metadata_for_acquisition_id(acq_ids, conn=None):
    pass


def get_all_acquisition_ids_for_study_id(study_id, conn=None):
    pass


def get_all_biomarkers_for_acquisition_id(acquisition_id, conn=None):
    pass
