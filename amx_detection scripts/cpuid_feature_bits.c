#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct _CPUID_REGISTERS {

    union {
        unsigned int Registers[4];
        struct {
            unsigned int Eax;
            unsigned int Ebx;
            unsigned int Ecx;
            unsigned int Edx;
        } Register;
    } x;

} CPUID_REGISTERS, *PCPUID_REGISTERS;

#define DISPLAY_SET_BITS 1
#define DISPLAY_CLEAR_BITS 2


void CpuidT_DisplayFeatureBits(unsigned int Subleaf, PCPUID_REGISTERS pCpuidRegisters, unsigned int Flags);
void CpuidT_DisplayFeatures(unsigned int Flags);


/*
 * main
 *
 * Entry Point
 *
 * Arguments:
 *     argc - Number of Arguements
 *     argv - Arguements 
 *     
 * Return:
 *     Zero
 */
int main(int argc, char **argv)
{
    printf("CPUID Leaf 7 Parser - Toby Opferman\n");
    printf(" 1 - Parse Local CPUID.7 for set bits\n");
    printf(" 2 - Parse Local CPUID.7 for clear bits\n");
    printf(" 3 - Prase Local CPUID.7 for set and clear bits\n");
    

    if (argc >= 2) 
    {
        switch (*argv[1]) 
        {
            case '1':
                CpuidT_DisplayFeatures(DISPLAY_SET_BITS);
                break;
            case '2':
                CpuidT_DisplayFeatures(DISPLAY_CLEAR_BITS);
                break;
            case '3':
                CpuidT_DisplayFeatures(DISPLAY_CLEAR_BITS | DISPLAY_SET_BITS);
                break;
        }
    }

    return 0;
}


/*
 * CpuidT_DisplaySubLeafs
 *
 * Reads leaf 7
 *
 * Arguments:
 *     None
 *     
 * Return:
 *     None
 */
void CpuidT_DisplayFeatures(unsigned int Flags)
{
    CPUID_REGISTERS CpuidRegisters;
    unsigned int Subleaf;
    unsigned int MaxSubleaf;

    __cpuidex(&CpuidRegisters.x.Registers[0], 0, 0);
    if (CpuidRegisters.x.Register.Eax >= 7) 
    {
        __cpuidex(&CpuidRegisters.x.Registers[0], 7, 0);
        MaxSubleaf = CpuidRegisters.x.Register.Eax;

        Subleaf = 0;
        while (Subleaf <= MaxSubleaf) 
        {
            __cpuidex(&CpuidRegisters.x.Registers[0], 7, Subleaf);
            printf("Leaf %08x Subleaf %u EAX: %08x EBX; %08x ECX: %08x EDX; %08x\n", 7, Subleaf, CpuidRegisters.x.Register.Eax, CpuidRegisters.x.Register.Ebx, CpuidRegisters.x.Register.Ecx, CpuidRegisters.x.Register.Edx);
            Subleaf++;
        } 

        Subleaf = 0;
        while (Subleaf <= MaxSubleaf) 
        {
            __cpuidex(&CpuidRegisters.x.Registers[0], 7, Subleaf);
            CpuidT_DisplayFeatureBits(Subleaf, &CpuidRegisters, Flags);
            Subleaf++;
        }
    }
}




unsigned char *pszArray[2][4][32] = {

    // Subleaf 0
    {
        // EAX
        {
            NULL, NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL
        },

        // EBX
        {

            "FSGSBASE. Supports RDFSBASE/RDGSBASE/WRFSBASE/WRGSBASE",
            "IA32_TSC_ADJUST MSR",
            "SGX. Intel Software Guard Extensions",
            "BMI1",
            "HLE",
            "AVX2",
            "FDP_EXCPTN_ONLY. x87 FPU Data Pointer updated only on x87 exceptions",
            "SMEP. Supervisor-Mode Execution Prevention",
            "BMI2",
            "Enhanced REP MOVSB/STOSB",
            "INVPCID",
            "RTM",
            "RDT-M. Intel Resource Director Technology",
            "Deprecates FPU CS and FPU DS values",
            "MPX. Supports Intel® Memory Protection Extensiona",
            "RDT-A. Intel Resource Director Technology (Intel® RDT) Allocation capability",
            "AVX512F",
            "AVX512DQ",
            "RDSEED",
            "ADX",
            "SMAP. Supervisor-Mode Access Prevention",
            "AVX512_IFMA",
            "Reserved Forever (Previously PCOMMIT)",
            "CLFLUSHOPT",
            "CLWB",
            "Intel Processor Trace",
            "AVX512PF. (Intel Xeon Phi only.)",
            "AVX512ER. (Intel Xeon Phi only.)",
            "AVX512CD",
            "SHA. Intel Secure Hash Algorithm Extensions (Intel® SHA Extensions)",
            "AVX512BW",
            "AVX512VL"
        },

        // ECX
        {
            "PREFETCHWT1. (Intel Xeon Phi only.)",
            "AVX512_VBMI",
            "UMIP. user-mode instruction prevention",
            "PKU. protection keys for user-mode pages if 1.",
            "OSPKE. OS has set CR4.PKE to enable protection keys",
            "WAITPKG (user Level Wait Support)",
            "AVX512_VBMI2",
            "CET_SS. CET shadow stack features. Processors that set this bit define bits 1:0 of the IA32_U_CET and IA32_S_CET MSRs. Enumerates support for the following MSRs: IA32_INTERRUPT_SPP_TABLE_ADDR, IA32_PL3_SSP, IA32_PL2_SSP, IA32_PL1_SSP, and IA32_PL0_SSP",
            "GFNI",
            "VAES",
            "VPCLMULQDQ", 
            "AVX512_VNNI",
            "AVX512_BITALG",
            "TME_EN. The following MSRs are supported: IA32_TME_CAPABILITY, IA32_TME_ACTIVATE,IA32_TME_EXCLUDE_MASK, and IA32_TME_EXCLUDE_BASE",
         	"AVX512_VPOPCNTDQ",
            "FZM",
            "LA57. Supports 57-bit linear addresses and five-level paging",
            "[21:17] The value of MAWAU used by the BNDLDX and BNDSTX instructions in 64-bit mode.",
            "[21:17] The value of MAWAU used by the BNDLDX and BNDSTX instructions in 64-bit mode.",
            "[21:17] The value of MAWAU used by the BNDLDX and BNDSTX instructions in 64-bit mode.",
            "[21:17] The value of MAWAU used by the BNDLDX and BNDSTX instructions in 64-bit mode.",
            "[21:17] The value of MAWAU used by the BNDLDX and BNDSTX instructions in 64-bit mode.",
            "RDPID and IA32_TSC_AUX are available",
            "KL. Key Locker",
            "BUS_LOCK_DETECT",
            "CLDEMOTE. cache line demote",
            "MPRR Available",
            "MOVDIRI.",
            "MOVDIR64B.",
            "Reserved. ENQCMD/S",
            "SGX_LC. SGX Launch Configuration",
            "PKS. protection keys for supervisor-mode pages"
        },

        // EDX
        {
            "Reserved. (SGX-TEM Trusted Execution Environment",
            "Reserved. (SGX-KEYS SGX Server Keying",
            "AVX512_4VNNIW. (Intel® Xeon Phi™ only.)",
            "AVX512_4FMAPS. (Intel® Xeon Phi™ only.)",
            "Fast Short REP MOV.",
            "UINTR - User Interrupts",
            "Reserved for PRT",
            "AVX512-BITALG2",
            "AVX512_VP2INTERSECT",
            "Reserved for PRT",
            "MD_CLEAR Reserved for PRT",
            "Reserved for PRT",
            "Reserved for PRT",
            "TSX_FORCE_ABORT MSR",
            "SERIALIZE",
            "Hybrid",
            "TSXLDTRK",
            "PaeSwSupported 32-bit Mode 62:52 Sofware Bits Available",
            "PCONFIG",
            "Architectural LBRs",
            "CET_IBT - Indirect branch tracking Processors that set this bit define bits 5:2 and bits 63:10 of the IA32_U_CET and IA32_S_CET MSRs",
            "DSP (Lakemont)",
            "AMX-BF16 - tile bfloat16 support",
            "AVX512-FP16",
            "AMX-TILES",
            "AMX-INT8 - tile 8-bit integer support",
            "indirect branch restricted speculation (IBRS) and the indirect branch predictor barrier (IBPB). Processors that set this bit support the IA32_SPEC_CTRL MSR and theIA32_PRED_CMD MSR. They allow software to set IA32_SPEC_CTRL[0] (IBRS) and IA32_PRED_CMD[0]",
            "single thread indirect branch predictors (STIBP). Processors that set this bit support the IA32_SPEC_CTRL MSR. They allow software to set IA32_SPEC_CTRL[1] (STIBP).",
            "L1D_FLUSH Processors that set this bit support the IA32_FLUSH_CMDand can set IA32_FLUSH_CMD[0]",
            "IA32_ARCH_CAPABILITIES",
            "IA32_CORE_CAPABILITIES",
            "Speculative Store Bypass Disable (SSBD). Processors that set this bit support the IA32_SPEC_CTRL MSR. They allow software to set IA32_SPEC_CTRL[2] (SSBD)."
        }

    },


    // Subleaf 1
    {
        // EAX
        {
            NULL,NULL,NULL,NULL,
            "AVX-VNNI",
            "AVX512_BF16",
            NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,
            "AMX-FP16",
            NULL,
            "AVX-IFMA",
            NULL,NULL,NULL,NULL,
            "AVX512-VMPSADBW / AVX512-VPDPWUSD[S]",
            NULL,NULL,NULL
        },

        // EBX
        {
            NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,
            "RAO_AVX512_FP",
            NULL
        },

        // ECX
        {
            NULL, NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL
        },

        // EDX
        {
         NULL,
         "AVX512-VNNI-FP16",
         "AVX512-VNNI-INT8",
         "AVX512-NE-CONVERT",
         "AVX-VNNI-INT8",
         "AVX-NE-CONVERT",
         "AMX-TRANSPOSE",
         "AMX-FP19",
         "AMX-COMPLEX",
         "AMX-AVX512",
         "AVX-VNNI-INT16",
         "AVX512-VNNI-INT16",
         NULL,NULL,NULL,NULL,
         "AVX512-BF16-NE",
         NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL
        }

    },
};


char *pszRegiterNames[] ={
    "EAX",
    "EBX",
    "ECX",
    "EDX"
};


void CpuidT_DisplayFeatureBits(unsigned int Subleaf, PCPUID_REGISTERS pCpuidRegisters, unsigned int Flags)
{   
    UINT RegisterIndex = 0;
    UINT BitIndex;

    if (Subleaf == 0) 
    {
        printf(" Max Subleafs = %i\n", pCpuidRegisters->x.Register.Eax);
        RegisterIndex = 1;
    }

    for (;RegisterIndex < 4; RegisterIndex++) 
    {
        for (BitIndex = 0; BitIndex < 32; BitIndex++) 
        {
            if ((1 << BitIndex) & pCpuidRegisters->x.Registers[RegisterIndex])
            {
                if (Flags & DISPLAY_SET_BITS) 
                {
                    if (pszArray[Subleaf][RegisterIndex][BitIndex] && Subleaf <= 1)
                    {
                        printf("CPUID.7.%i.%s[%i] = (true)%s\n", Subleaf, pszRegiterNames[RegisterIndex], BitIndex, pszArray[Subleaf][RegisterIndex][BitIndex]);
                    }
                    else
                    {
                        printf("CPUID.7.%i.%s[%i] = (true):No Description\n", Subleaf, pszRegiterNames[RegisterIndex], BitIndex);
                    }
                }
            }
            else
            {
                if (Flags & DISPLAY_CLEAR_BITS) 
                {
                    if (pszArray[Subleaf][RegisterIndex][BitIndex] && Subleaf <= 1)
                    {
                        printf("CPUID.7.%i.%s[%i] = (false): %s\n", Subleaf, pszRegiterNames[RegisterIndex], BitIndex, pszArray[Subleaf][RegisterIndex][BitIndex]);
                    }
                    else
                    {
                        printf("CPUID.7.%i.%s[%i] = (false):No Description\n", Subleaf, pszRegiterNames[RegisterIndex], BitIndex);
                    }
                }
            }
        }
    }
}




