import can
import cantools
import pandas as pd

def main():
	dbc_filename = 'dbc_data.dbc'
	blf_filename = 'blf_data.blf'
	#decoded_msg = []
	decoded_msg = pd.DataFrame()
	db = cantools.db.load_file(dbc_filename)

	with can.BLFReader(blf_filename) as can_log:
		for msg in can_log:
			#decoded_msg.append(db.decode_message(msg.arbitration_id, msg.data))
			add_msg = pd.DataFrame(data = db.decode_message(msg.arbitration_id, msg.data))
			decoded_msg = decoded_msg.append(data = add_msg)
	return

if __name__ == '__main__':
	main()