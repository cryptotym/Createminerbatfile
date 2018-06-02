# Createminerbatfile
Python script to create miner bat files for the best mining software
Created so you don't have to manually edit miner bat files.

# Step descriptions:

1. Enter coin name:
- This is just to tell the files apart for better usability, not important for function.

2. Enter the algorithm:
- Must be exactly how the mining software requires, if you are unsure run --help from your softare.

3. Enter the main pool and port (stratum+tcp://site.com:port):
- Be sure to enter the pool stratum AND port number in the format shown.

4. Enter the failover pool and port:
- Failover pool for when your first pool goes down cause we all know it will at some point.

5. Enter the wallet receiving address:
- Simply paste your receiving address.

6. Enter the coin symbol:
- Use the coin symbol labeled on the pool, ie for Raven enter RVN

7. Enter rig identifier name:
- Just to tell your rigs apart on the pool if you're using more than one machine, makes troubleshooting easier. You can input anything.

8. Enter intesity(Choose a number between 16-21):
- This is the intensity, I typically run 21, but your rigs may only be able to handle 20 or if lyra2z only 16.
