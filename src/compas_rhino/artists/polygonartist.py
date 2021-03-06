from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

# import compas_rhino
from compas_rhino.artists.primitiveartist import PrimitiveArtist


__all__ = ['PolygonArtist']


class PolygonArtist(PrimitiveArtist):
    """Artist for drawing polygons.

    Parameters
    ----------
    polygon : :class:`compas.geometry.Polygon`
        A COMPAS polygon.

    Other Parameters
    ----------------
    See :class:`compas_rhino.artists.PrimitiveArtist` for all other parameters.

    Examples
    --------
    >>>

    """

    def draw(self):
        """Draw the polygon.

        Returns
        -------
        list
            The GUIDs of the created Rhino objects.
        """
        raise NotImplementedError


# ==============================================================================
# Main
# ==============================================================================

if __name__ == "__main__":

    pass
