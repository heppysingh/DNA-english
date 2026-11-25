# **D.N.A**

#### **Beta DNA3 Released**
#### **Introduction**

1. Full name: **Droid Normal Assistant** (Android General Firmware Unpack/Repack Assistant), abbreviated as **D.N.A**

2. Supports common formats (`*.zip, *.br, *.dat, *.dat.1~20, ext4/2 *.img, payload.bin, *.win000-004`). Detected by file extension only — any filename works!

3. Supports unpacking Android 5.0+ firmware, including Android 11 `vendor.img` unpacking
   - Tested ROM (Mi 10 Pro): [_miui_CMI_20.11.19_a7ff2a5b4e_11.0.zip_](https://hugeota.d.miui.com/20.11.19/miui_CMI_20.11.19_a7ff2a5b4e_11.0.zip)

4. Supports Android [5.0+] **Non-Dynamic & Dynamic Partition** repacking (_flash testing not performed due to lack of a dynamic-partition device_) ---- 2020.12.20
   - Android [5.0~8.1] uses `_make_ext4fs_` to repack `.img`!
   - Android [9.0+] uses `_mke2fs + e2fsdroid_` to repack `.img`!
   - Tested ROM (Mi 10 Pro): [_miui_CMI_20.12.10_a0bb9661ec_11.0.zip_](https://hugeota.d.miui.com/20.12.10/miui_CMI_20.12.10_a0bb9661ec_11.0.zip) ---- 2020.12.20

5. Supports merging split `*.dat.*` files, up to 20 segments (1~20; several checked vivo ROMs typically have 15 split files, more would slow down unpacking)
   - Tested ROM (vivo Y9s): [_PD1945_A_1.10.7-update-full_1589940104.zip_](http://sysupwrdl.vivo.com.cn/upgrade/official/officialFiles/PD1945_A_1.10.7-update-full_1589940104.zip) ---- 2020.11.22

6. Supports unpacking `payload.bin` and automatically finding and extracting all ext2/4 images in one go!
   - Tested ROM (OnePlus 8 Pro): [_OnePlus8ProHydrogen_15.Y.14_OTA_0140_all_2010200027_1bc1714063af44ff.zip_](https://download.h2os.com/OnePlus8Pro/OBT/OnePlus8ProHydrogen_15.Y.14_OTA_0140_all_2010200027_1bc1714063af44ff.zip) ---- 2020.11.22

7. Supports unpacking TWRP backup files (excluding `data`), up to 4 segments (`*.win000~004`) ---- 2020.11.24

8. PC Linux version public beta ---- 2020.11.30

9. Added plugin support; relative plugin path: `DNA/Insides/Errors/submodules` (public beta) ---- 2020.12.21

10. Added MagiskBootKitchen (Android-Image-Kitchen) to unpack/repack `[boot|exaid|recovery/etc].img` ---- 2024.4.4

11. Supports unpacking and repacking **Dynamic A-only, Dynamic A/B (including dual-slot), and Virtual A/B** `super.img` files:
    - Automatically saves the original `super.img` metadata layout (`super_info.json`: size, alignment, slot count, groups, and partition attributes) during unpacking and reuses it when repacking.
    - Supports multi-slot metadata selection, `ZERO` extents, and sparse/raw `super.img` images.
    - Manual slot mode can also be configured in Settings (`[77]` → `IS_VAB`: `0=A-only`, `1=Virtual A/B`, `2=Dynamic A/B`).

12. Fixed inaccurate size detection for some dynamic partitions! ---- 2021.01.09

13. Fixed errors when repacking with `_make_ext4fs_`! ---- 2021.01.21

14. Added quiet mode for repacking (automatically repacks all packable items in the project directory without prompting) ---- 2021.01.21


#### **Supported Architectures**

1. Android Termux ARM64 (`aarch64`) (Natively supports Termux — no container required!)

2. Windows 10 PC `x86_64` (`x64`)

3. Virtual machine or bare-metal Ubuntu 20.04+ `x86_64` (`x64`) (Recommended!)


#### **Installation Guide (PC users start from Step 5; each line is a single complete command)**


1. Install the official [Termux.apk](https://search.f-droid.org/?q=termux) on your phone, launch Termux, and grant storage permissions:
   - `termux-setup-storage`

###### Native Termux support — no container needed!

5. Open Ubuntu / Linux / Termux (**PC guide starts here; mobile users continue below**) — copy and run in terminal:
   - `sudo apt update && sudo apt upgrade -y` (*Required. If this fails due to mirror issues, restore `/etc/apt/sources.list` from backup and retry.*)
   - `sudo apt install git cpio aria2 brotli android-sdk-libsparse-utils openjdk-11-jre p7zip-full -y` (*Required; recommended to re-run before using a new version.*)

   - ~`sudo apt install zip unzip gawk sed curl wget -y`~ [Optional, not required]

6. Clone this tool (copy and run in terminal):
   - `git clone https://github.com/ColdWindScholar/DNA3 -b feature --depth 1` (**Latest DNA3 public beta**)

7. After downloading, run:
   - `cd DNA && python3 dna.py`

8. The tool is now running — setup complete!
   - 1. To start it later, simply open Termux and enter `ubuntu` (if using proot Ubuntu and the tool is installed).
   - 2. If you want Termux to auto-start on launch, run the following in Termux (outside proot Ubuntu; restart Termux first):
        `echo -e "if [ -d ubuntu ] && [ $(command -v ubuntu) ]; then\n\tubuntu\nfi" >> .bashrc`
        Then restart Termux.


#### **Usage Notes**

1. Inside Termux, try **NOT to use system root**. On PC, root privileges (`sudo`) may be required, though it is best not to run while logged in directly as the `root` user to avoid permission issues after flashing!

2. The tool checks for updates online on startup, which may take a moment; if you use it frequently, avoid exiting unnecessarily.

3. **Unpacking ZIP files on mobile**:
   - Place `.zip` files in **internal storage `/sdcard/Download`** and the tool will automatically find them; otherwise place them in the tool's directory.

4. Tool directory under Termux proot Ubuntu on mobile: **`/data/data/com.termux/files/home/ubuntu/root/DNA`**

5. **Do NOT delete the `<project_dir>/configs` folder** — it contains all metadata required for repacking. To change the repacked `.img` size, open `<project_dir>/configs/*_size.txt` and edit the value in bytes. If a dynamic partition exceeds its size, you can also edit both `<project_dir>/configs/*_size.txt` and `dynamic_partitions_op_list` (e.g., `resize vendor ~2016763904~`). Booting is not guaranteed on dynamic-partition devices since no test device was available.

6. Depending on phone performance, proot overhead, and how the tool operates (**for example, comparing and updating `fs_config` for newly added files before repacking**), the tool may appear frozen — please be patient and wait a moment.

7. When deleting files, prefer running `rm -rf <file_or_folder>` inside Termux or proot Ubuntu (**do NOT use system root**).

8. **Do NOT run inside folders with non-ASCII/Chinese names, do NOT select files with spaces in their names, and do NOT use spaces or special characters in project folder names!**

9. Updating: Delete the old `DNA` folder (back up any important files/plugins first) and run:
   `git clone https://github.com/ColdWindScholar/D.N.A3 --depth 1`

10. **Dynamic partitions must be repacked into the official recovery flashable `.zip` format** (repacked as `.new.dat.br` or `.new.dat` together with `dynamic_partitions_op_list` inside the project folder); flashing standalone `.img` files is not supported.

11. If you use **system ROOT** on mobile to modify files in a project directory (e.g., **adding or editing files**), remember to set full **`777`** permissions on the modified files/folders!

#### **Previews**

![Image text](https://gitee.com/wenrou2554/dna_gitee/raw/master/views/2_view_x86_64.png)
![Image text](https://gitee.com/wenrou2554/dna_gitee/raw/master/views/3_view_x86_64.png)
![Image text](https://gitee.com/wenrou2554/dna_gitee/raw/master/views/4_view_x86_64.png)


#### **Community & Feedback**

1. QQ Group 1: [MIO-KITCHEN Official Group 2](https://qm.qq.com/q/1UFWpnuiIY)
2. QQ Group 2: [DNA3](https://qm.qq.com/q/VE8gFAXZaq)

#### **Disclaimer**

1. This tool runs in a Termux proot environment and does not require root privileges. **Please do NOT use system root in Termux!**

2. This tool contains NO malicious code (no system damage, data theft, etc.)!

3. **The author assumes NO responsibility for any data loss or corruption caused by users modifying project directories with root privileges!**

#### [D.N.A3](https://github.com/ColdWindScholar/D.N.A3)
#### ColdWindScholar (3590361911@qq.com). All rights reserved.
