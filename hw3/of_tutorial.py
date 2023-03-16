from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()



class Tutorial (object):
  def __init__ (self, connection):
    self.connection = connection
    connection.addListeners(self)

    self.mac_to_port = {}


  def resend_packet (self, packet_in, out_port):

    msg = of.ofp_packet_out()
    msg.data = packet_in
    action = of.ofp_action_output(port = out_port)
    msg.actions.append(action)

    self.connection.send(msg)


  def act_like_hub (self, packet, packet_in):
    self.resend_packet(packet_in, of.OFPP_ALL)
    
  def act_like_switch (self, packet, packet_in):
    if packet.src not in self.mac_to_port:
      #print("Learning that " + str(packet.src) + " is attached at port " + str(packet_in.in_port))
      self.mac_to_port[packet.src] = packet_in.in_port
    # if the port associated with the destination MAC of the packet is known:
    if packet.dst in self.mac_to_port:
    # Send packet out the associated port
      #print(str(packet.dst) + " destination known. only send message to it")
      self.resend_packet(packet_in, self.mac_to_port[packet.dst])
    else:
    # Flood the packet out everything but the input port
    # This part looks familiar, right?
      #print(str(packet.dst) + " not known, resend to everybody")
      self.resend_packet(packet_in, of.OFPP_ALL)

  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    #log.info("Switch observing traffic: %s" % (self.connection))
    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.

    self.act_like_switch(packet, packet_in)



def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Tutorial(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
