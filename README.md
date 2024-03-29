# Depth-Estimation
A prototype for depth-estimation using Depth-Anything



#### How to Run: 
1.  Clone the repository:

   ```bash
   git clone https://github.com/FaceFindr/Depth-Estimation.git
   cd Depth-Estimation
   ````

2. Install the required packages
    ```` bash
   pip install -r requirements.txt
   ````

3. Example to Create a Depth map:
```bash
    python run.py --encoder vitl --img-path assets/examples2 --outdir assets/results2
```

4. To crop an image
```bash
    python crop.py --img-path assets/results2/demo17.png --x 400 --y 800 --width 500 --height 500 --outdir assets/results2
``` 


5. To check the average depth of an image
```bash
    python depth.py --img-path assets/results2/demo17.png
``` 
