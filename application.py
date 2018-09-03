class Application(object):
  """ Represents an application running on a cube. """

  def run(self, cube):
    """ Runs the application on a particular cube.
    Args:
      cube: A handle to the cube that this app is running on. """
    self.__cube = cube

  def on_reconfiguration(self, config):
    """ This is a stub method that will be called every time the connection
    configuration of the cube that this application is running on changes. By
    default, it does nothing.
    Args:
      config: The new configuration, as returned by Cube.get_connections(). """
    return
