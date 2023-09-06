from icmplib import ping

class IcmpPing:
	def __init__(self, hostaddress, **kwargs):
		self._hostaddress=hostaddress
		self._kwargs = kwargs

	def __iter__(self):
		host = ping(self._hostaddress, **self._kwargs)
		data = [ {
			"instance": self._hostaddress,
			"is_alive": int(host.is_alive),
			"avg_rtt": host.avg_rtt,
			"max_rtt": host.max_rtt,
			"min_rtt": host.min_rtt,
			"packet_loss": host.packet_loss,
			"packets_received": host.packets_received,
			"packets_sent": host.packets_sent
		}]
		return iter(data)
