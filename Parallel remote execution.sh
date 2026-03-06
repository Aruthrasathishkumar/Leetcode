servers=(...)
max_jobs=10

remote_task() { ssh "$server" 'uptime; df -h'; }

for server in "${servers[@]}"; do
  while [ "$(jobs -r | wc -l)" -ge "$max_jobs" ]; do
    sleep 0.1
  done
  remote_task "$server" &
done
wait