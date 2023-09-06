{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'data.txt'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[39m# create me the code to read txt files\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[39m# read file\u001b[39;00m\n\u001b[1;32m----> 3\u001b[0m f \u001b[39m=\u001b[39m \u001b[39mopen\u001b[39;49m(\u001b[39m'\u001b[39;49m\u001b[39mdata.txt\u001b[39;49m\u001b[39m'\u001b[39;49m, \u001b[39m'\u001b[39;49m\u001b[39mr\u001b[39;49m\u001b[39m'\u001b[39;49m)\n\u001b[0;32m      4\u001b[0m \u001b[39mprint\u001b[39m(f\u001b[39m.\u001b[39mread())\n\u001b[0;32m      5\u001b[0m f\u001b[39m.\u001b[39mclose()\n",
      "File \u001b[1;32m~\\AppData\\Roaming\\Python\\Python311\\site-packages\\IPython\\core\\interactiveshell.py:286\u001b[0m, in \u001b[0;36m_modified_open\u001b[1;34m(file, *args, **kwargs)\u001b[0m\n\u001b[0;32m    279\u001b[0m \u001b[39mif\u001b[39;00m file \u001b[39min\u001b[39;00m {\u001b[39m0\u001b[39m, \u001b[39m1\u001b[39m, \u001b[39m2\u001b[39m}:\n\u001b[0;32m    280\u001b[0m     \u001b[39mraise\u001b[39;00m \u001b[39mValueError\u001b[39;00m(\n\u001b[0;32m    281\u001b[0m         \u001b[39mf\u001b[39m\u001b[39m\"\u001b[39m\u001b[39mIPython won\u001b[39m\u001b[39m'\u001b[39m\u001b[39mt let you open fd=\u001b[39m\u001b[39m{\u001b[39;00mfile\u001b[39m}\u001b[39;00m\u001b[39m by default \u001b[39m\u001b[39m\"\u001b[39m\n\u001b[0;32m    282\u001b[0m         \u001b[39m\"\u001b[39m\u001b[39mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[39m\"\u001b[39m\n\u001b[0;32m    283\u001b[0m         \u001b[39m\"\u001b[39m\u001b[39myou can use builtins\u001b[39m\u001b[39m'\u001b[39m\u001b[39m open.\u001b[39m\u001b[39m\"\u001b[39m\n\u001b[0;32m    284\u001b[0m     )\n\u001b[1;32m--> 286\u001b[0m \u001b[39mreturn\u001b[39;00m io_open(file, \u001b[39m*\u001b[39;49margs, \u001b[39m*\u001b[39;49m\u001b[39m*\u001b[39;49mkwargs)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'data.txt'"
     ]
    }
   ],
   "source": [
    "\n",
    "# create me the code to read txt files\n",
    "# read file\n",
    "f = open('data.txt', 'r')\n",
    "print(f.read())\n",
    "f.close()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
