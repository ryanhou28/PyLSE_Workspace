set search_path [ list "./" "/afs/umich.edu/class/eecs470/lib/synopsys/" ]
set target_library "lec25dscc25_TT.db"
set link_library [concat  "*" $target_library]

set verilog_files [list ps.sv]

set top_level ps