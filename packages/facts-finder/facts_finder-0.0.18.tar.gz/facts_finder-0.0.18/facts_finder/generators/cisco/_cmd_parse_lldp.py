"""cisco show lldp neighbour command output parser """

# ------------------------------------------------------------------------------
from nettoolkit import *
from facts_finder.generators.commons import *
from .common import *
# ------------------------------------------------------------------------------

def get_lldp_neighbour(cmd_op, *args, dsr=True):
	"""parser - show lldp neigh command output

	Parsed Fields:
		* port/interface
		* neighbor interface
		* neighbor hostname

	Args:
		cmd_op (list, str): command output in list/multiline string.
		dsr (bool, optional): DOMAIN SUFFIX REMOVAL. Defaults to True.

	Returns:
		dict: output dictionary with parsed fields
	"""
	cmd_op = verifid_output(cmd_op)
	nbr_d, remote_hn = {}, ""
	nbr_table_start = False
	for i, line in enumerate(cmd_op):
		line = line.strip()
		dbl_spl = line.split("  ")
		if line.startswith("Device ID"): 
			nbr_table_start = True
			continue
		if not nbr_table_start: continue
		if not line.strip(): continue				# Blank lines
		if line.startswith("Total "): continue		# Summary line
		if line.startswith("!"): continue			# Remarked line

		### NBR TABLE PROCESS ###

		# // LOCAL/NBR INTERFACE, NBR PLATFORM //
		# // NBR HOSTNAME //
		local_if = STR.if_standardize(line[20:31].strip().replace(" ", ""))
		remote_if = STR.if_standardize(dbl_spl[-1].strip())
		remote_hn = line[:20].strip()
		if dsr: remote_hn = remove_domain(remote_hn)

		# SET / RESET
		nbr_d[local_if] = {'neighbor': {}}
		nbr = nbr_d[local_if]['neighbor']
		nbr['hostname'] = remote_hn
		nbr['interface'] = remote_if
		remote_hn, remote_if, local_if = "", "", ""
	# print(nbr_d)
	return nbr_d
# ------------------------------------------------------------------------------
