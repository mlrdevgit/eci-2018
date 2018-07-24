# Arquitectura de software

Notas:
- Aprendan:
- ¿Qué componentes se utilizan para usar GPUs?
- ¿De dónde los consigo?
- ¿Qué diferencias hay entre distintas arquitecturas?


## Arquitectura componentizada

<img src='images/arquitecture-soft.png' style='height:420px' />


## Arquitectura componentizada (app)

- Scripts
- Aplicación
- Engine
- Runtime

Notas:
- Qué hace cada componente
- Quién provee cada componente
- Qué alternativas hay
- Cómo funcionan las dependencias
- Scripts: lógica particular (nivel), efectos
- Aplicación: orquestrar todo, lógica particular
- Engine: lógica general (física, render, red, disco)
- Runtime: manejo de recursos, compatibilidad, reglas (OpenGL)


## Arquitectura componentizada (OS)

- Runtime
- Driver (user mode)
- Driver (kernel mode)
- Kernel

Notas:
- Qué hace cada componente
- Quién provee cada componente
- Qué alternativas hay
- Cómo funcionan las dependencias
- Runtime: manejo de recursos, compatibilidad, reglas (OpenGL)
- Driver (user mode): manejo de recursos, compilación, sincronizacón (a veces)
- Driver (kernel mode): manejo de recursos coordinados, sincronización, ejecución - Dxgkrnl.sys
- Kernel: manejo de drivers, hardware, modelo de driver


## Extras del sistema operativo

- Compositor: coordinación de presentación, efectos (Compiz)
- Drivers y dispositivos de display: especialmente casos remotos, virtualización
- Transiciones de hardware: UI, adquisición drivers
- MSBDD: driver de display sin IHV (Microsoft Basic Display Driver)
- WARP: driver de D3D en software (Windows Advanced Rasterization Platform) (OpenSWR)

Notas:
- Qué hace cada componente
- MSBDD funciona sobre BIOS/UEFI
- WARP funciona sobre el CPU con algunas familias de vectorización


## Ejemplos de stack - WDDM - kernel

[Driver Model Design Guide](https://docs.microsoft.com/en-us/windows-hardware/drivers/display/windows-vista-display-driver-model-design-guide)

```C++
NTSTATUS DxgkDdiAddDevice(
  _In_  const PDEVICE_OBJECT PhysicalDeviceObject,
  _Out_       PVOID          *MiniportDeviceContext
)

NTSTATUS APIENTRY DxgkDdiCreateDevice(
  _In_    const HANDLE               hAdapter,
  _Inout_       DXGKARG_CREATEDEVICE *pCreateDevice
)

typedef struct _DXGKARG_CREATEDEVICE {
  HANDLE hDevice;
  union {
    DXGK_CREATEDEVICEFLAGS Flags;
    DXGK_DEVICEINFO        *pInfo;
  };
#if (DXGKDDI_INTERFACE_VERSION >= DXGKDDI_INTERFACE_VERSION_WDDM2_0)
  ULONG  Pasid;
  HANDLE hKmdProcess;
#endif 
} DXGKARG_CREATEDEVICE;
```

Notas:
- DriverEntry ("main") es donde el driver registra sus funciones de callback
- Luego varias funciones se van llamando, por ejemplo AddDevice para crear un
  hAdapter, CreateDevice para crear un hDevice


## Ejemplos de stack - WDDM - modo usuario

```C++
__checkReturn HRESULT APIENTRY CreateDevice(
  _In_    HANDLE                 hAdapter,
  _Inout_ D3DDDIARG_CREATEDEVICE *pCreateData
)

typedef struct _D3DDDIARG_CREATEDEVICE {
  HANDLE                       hDevice;
  UINT                         Interface;
  UINT                         Version;
  const D3DDDI_DEVICECALLBACKS *pCallbacks;
  VOID                         *pCommandBuffer;
  UINT                         CommandBufferSize;
  D3DDDI_ALLOCATIONLIST        *pAllocationList;
  UINT                         AllocationListSize;
  D3DDDI_PATCHLOCATIONLIST     *pPatchLocationList;
  UINT                         PatchLocationListSize;
  D3DDDI_DEVICEFUNCS           *pDeviceFuncs;
  D3DDDI_CREATEDEVICEFLAGS     Flags;
#if (D3D_UMD_INTERFACE_VERSION >= D3D_UMD_INTERFACE_VERSION_WIN7)
  D3DGPU_VIRTUAL_ADDRESS       CommandBuffer;
#endif 
} D3DDDIARG_CREATEDEVICE;
```

Notas:
- https://msdn.microsoft.com/library/windows/hardware/ff540634
- comparativamente una serie de operaciones
- permite que exista estado en modo usuario, mejora performance
- termina funcionande en base a llamadas a modo kernel para conseguir
  distintos objetos
- mismo diseño de tabla de funciones en pDeviceFuncs


## Ejemplos de stack - runtime

- CreateDXGIFactory(...)
- IDXGIFactory
 - CreateSoftwareAdapter
 - CreateSwapChain (ForHwnd/CoreWindow/Composition)
 - EnumAdapters
 - GetWindowAssociation
 - MakeWindowAssociation
- IDXGIAdapter
 - CheckInterfaceSupport
 - EnumOutputs
 - GetDesc

Notas:
- Otros objetos: resource, surface, output, swapchain.
- Enumeración, creación, extensibilidad, interoperabilidad
- Qué no hace: compatibilidad, sincronización, formatos especializados,
  ejecución
- https://msdn.microsoft.com/en-us/library/windows/desktop/bb174535(v=vs.85).aspx


## Ejemplos de stack - runtime

```C++
D3D11CreateDevice(...)

HRESULT D3D11CreateDevice(
  _In_opt_        IDXGIAdapter        *pAdapter,
                  D3D_DRIVER_TYPE     DriverType,
                  HMODULE             Software,
                  UINT                Flags,
  _In_opt_  const D3D_FEATURE_LEVEL   *pFeatureLevels,
                  UINT                FeatureLevels,
                  UINT                SDKVersion,
  _Out_opt_       ID3D11Device        **ppDevice,
  _Out_opt_       D3D_FEATURE_LEVEL   *pFeatureLevel,
  _Out_opt_       ID3D11DeviceContext **ppImmediateContext
);
```

Notas:
- Conexión con adaptadores
- Rasterizador de software o hardware
- Feature level - más adelante, evitar 'feature bits' infinitos
- SDK version, compatibilidad
- Device y feature levels finales
- Immediate context - más adelante


## Arquitectura monolítica

- Fusión de capas:
 - user mode y kernel mode
 - aplicación o runtime con engine
 - compositor virtualizado o exclusivamente por hardware
 - precompilado de scripts, shaders

Notas:
- Por ejemplo en consolas o dispositivos embebidos.

## Ejercicio - Composición

Composición está activa en Windows.

```
tasklist | findstr dwm.exe
```

Notas:
- Proceso con privilegios, necesita admin mode para enumerarlo.

## Ejercicio - notepad

Busquen componentes con debugger or procexp: `windbg notepad.exe`

Notas:
- Ver que no hay DX cargado directamente (uso de GDI).
- Ctrl O para abrir explorer en el proceso a través del diálogo de archivos.

```
lm md3d*
lmv md3d11
lmv mdxgi
lmv mdcomp
~*k
```

- No hay driver! Pero en Firefox...


## Ejercicio - Firefox

Tada! `nvinitx.dll`

Notas:
- C:\WINDOWS\System32\DriverStore\FileRepository\nvmso.inf_amd64_b89aa41766002e30\nvinitx.dll
- lm es para ver módulos
- lmf se usa para ver los archivos
- notepad usa GDI
- explorer usa D3D, pero no necesariamente va a estar corriendo
- cuando aparece D3D, van a ver que aparece DXGI, pero no hizo falta cargar todos los drivers


## Ejercicio - dwm

Corriendo procexp en https://live.sysinternals.com/procexp.exe, ver dwm.exe, bajo winlogon.exe.

Notas:
- asegúrense de correr en modo administrador, desde 'File', 'Show Details for all processes'


## Ejercicio - Win10 - Task Manager

En Windows 10, Task Manager, GPU, vean el consume mientras mueven la ventana.

Notas:
- acá pueden ver cómo dwm es el que está haciendo uso directo del GPU
- todo lo demás termina ocurriendo en modo usuario por composición o a través de GDI
- con un juego verían el uso de GPU, mismo con uso de compute


## Ejercicio - Device Manager

Driver - driver details

Notas:
- Qué otros archivos hay? OpenGL? GLES? OpenCL? Media codecs?
- OpenGL, OpenCL, libGLES
- dxva para video
- Device Instance Path - jerarquía de buses y dispositivos tipo PnP
- Class Guid - qué tipo es, a quién le interesa y con qué se conecta
- Bus reported (Video Controller)
- Display Name
- Physical Device Object name


## Preguntas sobre arquitectura


