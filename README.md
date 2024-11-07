
## Question 1
Django signals are executed synchronously. This means that when a signal is sent, all connected receiver functions are called immediately and must complete before the next step in the process can proceed.

The output sequence indicates that:
1) The signal receiver starts processing immediately after the 2) User instance is saved.
3) The main thread waits for the receiver to complete its task before printing "User save operation complete."

## Question 2
Django signals execute in the same thread as the caller. This means that when a signal is sent, all connected receiver functions are invoked within the same thread that dispatched the signal.

When this script runs, the output will be:

#### Signal handler thread ID: 140735218000896
#### Main thread ID: 140735218000896


The identical thread IDs confirm that both the signal handler and the main execution flow operate within the same thread. This behavior is consistent with Django's default synchronous signal processing.

## Question 3
Django signals execute within the same database transaction as the caller. This means that if a signal is triggered during a transaction, the operations performed within the signal handler are part of that transaction. Consequently, if the transaction is rolled back, the changes made by the signal handler are also rolled back.


