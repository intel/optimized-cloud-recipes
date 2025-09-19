
<p align="center">
  <img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/logo-classicblue-800px.png?raw=true" alt="Intel Logo" width="250"/>
</p>

# Intel® Advanced Matrix Extensions (Intel® AMX)

© Copyright 2025, Intel Corporation

## Overview

This document showcases how to validate that Intel® AMX is enabled and being utilized by the application.

**These instructions apply to Ubuntu 22.04 and later.**

## Accelerate AI Workloads with Intel® AMX

Intel® AMX is built into Intel® Xeon 4th, 5th, and 6th Generation Scalable processors. It is a new built-in accelerator that improves the performance of deep-learning training and inference on the CPU. Intel® AMX is ideal for AI workloads acceleration.

Intel Xeon 4th generation and above are available in most cloud service providers, including AWS, Azure, and GCP.

For more see [Intel® AMX](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html)

### Validate Intel® AMX is enabled

SSH to the system and run the following command to check if Intel® AMX is enabled:

```bash
lscpu | grep amx
```

**You should notice three flags: amx_bf16 amx_tile amx_int8** (towards the end)

Flags:

fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon rep_good nopl xtopology nonstop_tsc cpuid aperfmperf tsc_known_freq pni pclmulqdq monitor ssse3 fma cx16 pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch ssbd ibrs ibpb stibp ibrs_enhanced fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid avx512f avx512dq rdseed adx smap avx512ifma clflushopt clwb avx512cd sha_ni avx512bw avx512vl xsaveopt xsavec xgetbv1 xsaves avx_vnni avx512_bf16 wbnoinvd ida arat avx512vbmi umip pku ospke waitpkg avx512_vbmi2 gfni vaes vpclmulqdq avx512_vnni avx512_bitalg tme avx512_vpopcntdq rdpid cldemote movdiri movdir64b md_clear serialize **amx_bf16** avx512_fp16 **amx_tile** **amx_int8** flush_l1d arch_capabilities

### Validate Intel® AMX is being utilized by the application

#### 1.Install processwatch

```bash
cd ~
# Install Git
sudo apt-get install git -y

# Install Processwatch
mkdir simd_experiment && cd $_
git clone --recursive https://github.com/intel/processwatch.git
cd processwatch/
sudo apt-get install libelf-dev cmake clang llvm llvm-dev libomp-dev build-essential binutils-dev libcapstone-dev libbpf-dev -y
./build.sh
sudo ln -sf `realpath processwatch` /usr/local/bin/
```

#### 2.Start processwatch

```bash
# Start the processwatch tool
sudo processwatch -f AMX_TILE

# For additional info 
sudo processwatch -f SSE -f AVX -f AVX2 -f AVX512 -f AMX_TILE
```

#### 3.Run your AI workload while monitoring the AMX_TILE

<img src="https://github.com/intel/optimized-cloud-recipes/blob/main/images/amx.png?raw=true" alt="AMX" width="350"/>

**Anything above 0.00, means that the application is utilizing Intel® AMX. The overall value is not very important, but the change in the value is.**

## References

- [Profiling Code To Check For Utilization of Intel® AMX Instructions](https://community.intel.com/t5/Blogs/Tech-Innovation/Cloud/Profiling-Code-To-Check-For-Utilization-of-Intel-AMX/post/1523871)
- [Processwatch](<https://github.com/intel/processwatch>)
- [Intel® AMX](https://www.intel.com/content/www/us/en/products/docs/accelerator-engines/advanced-matrix-extensions/overview.html)
