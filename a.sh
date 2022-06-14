while [ true ]
do
if [[ "$server_orig_host_hostname" != "$client_orig_host_hostname" ]]
then
    >&2 echo "Executing the client for $ITER_DURATION second(s)..."
    ./client $SERVER_IP $SERVER_PORT $TEST_SET $ITER_DURATION
else
    >&2 echo "new client_orig_host_hostname: $client_orig_host_hostname"

    while ! echo "1" | netcat -q 0 $SERVER_IP $NETCAT_PORT
    do # Reset server
        sleep 0.1 # dumb solution
    done
    >&2 echo "Requesting to the server to reset"

    server_ret = $(netcat -l $NETCAT_PORT) # Wait server
    >&2 echo "The server has responded!"

    while [ true ]
    do
        >&2 echo "Executing the 'libusernet'-attached client for $ITER_DURATION second(s)..."
        LD_PRELOAD="libsyscall_intercept.so ./libusernet.so" ./client $SERVER_IP $SERVER_PORT $TEST_SET $ITER_DURATION
    done
fi
client_orig_host_hostname=$(./vsock_client $VSOCK_PORT) # Get client-side current host's hostname
done