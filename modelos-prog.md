-*- mode: markdown; coding: utf-8 -*-

# Modelos de programación


## Indirección de programas

- GLSL/DirectX: shaders como objetos/assets
- CUDA y Metal intentan borrar el uso.

Notas:
- GPU no es directamente programable.
- El compilar de CPU no es el mismo que el de GPU.
- Distintos lenguajes, distintas operaciones, distintos modelos.
- CUDA y Metal intentan borrar el uso.


## Invocaciones en DirectX

```C++
int __cdecl main() {
 // Crear dispositivo.
 CreateComputeDevice( &g_pDevice, &g_pContext, false );
 // Crear shader (suma dos arrays).
 CreateComputeShader( L"BasicCompute11.hlsl", "CSMain", g_pDevice, &g_pCS );
 // Inicializar datos, crear recursos (structured buffers), crear vistas (views).
 for ( int i = 0; i &lt; NUM_ELEMENTS; ++i ) {
  g_vBuf0[i].i = i; // BufType *
  g_vBuf1[i].i = i; 
 }

 CreateStructuredBuffer( g_pDevice, sizeof(BufType), NUM_ELEMENTS, &g_vBuf0[0], &g_pBuf0 ); 
 CreateStructuredBuffer( g_pDevice, sizeof(BufType), NUM_ELEMENTS, &g_vBuf1[0], &g_pBuf1 ); 
 CreateStructuredBuffer( g_pDevice, sizeof(BufType), NUM_ELEMENTS, nullptr, &g_pBufResult ); 

 CreateBufferSRV( g_pDevice, g_pBuf0, &g_pBuf0SRV ); 
 CreateBufferSRV( g_pDevice, g_pBuf1, &g_pBuf1SRV ); 
 CreateBufferUAV( g_pDevice, g_pBufResult, &g_pBufResultUAV ); 

 // Ejecutar shader 
 ID3D11ShaderResourceView* aRViews[2] = { g_pBuf0SRV, g_pBuf1SRV }; 
 RunComputeShader( g_pContext, g_pCS, 2, aRViews, nullptr, nullptr, 0, g_pBufResultUAV, NUM_ELEMENTS, 1, 1 ); 

 // Leer resultados y verificar.
 { 
  ID3D11Buffer* debugbuf = CreateAndCopyToDebugBuf( g_pDevice, g_pContext, g_pBufResult ); 
  D3D11_MAPPED_SUBRESOURCE MappedResource;
  g_pContext->Map( debugbuf, 0, D3D11_MAP_READ, 0, &MappedResource );
  VerifyBufferValues((BufType*)MappedResource.pData);
  g_pContext->Unmap( debugbuf, 0 ); 
  SAFE_RELEASE( debugbuf );
 } 

 // Clean up.
 return 0; 
}
```

Notas:
- Por ejemplo, para correr un programa de compute.


## Invocaciones en CUDA

- Se puede escribir directamente con el programa (poco frecuente en la práctica).
- nvcc reescribo el código de C para hacer las invocaciones como en DX (opcional pero lo más común)
- Compila a PTX


## Invocaciones en CUDA

```C++
// Kernel definition
__global__ void VecAdd(float* A, float* B, float* C) {
  int i = threadIdx.x;
  C[i] = A[i] + B[i];
}

int main() {
 // Inicializar el dispositivo es opcional.
 // Inicializar datos, crear recursos (device memory).
 float* h_A = (float*)malloc(size);
 float* h_B = (float*)malloc(size);
 for ( int i = 0; i &lt; NUM_ELEMENTS; ++i ) { h_A = h_B = i; }

 // Esto va a device memory, se copia, y luego invocamos kernel.
 float* d_A; cudaMalloc(&d_A, size);
 float* d_B; cudaMalloc(&d_B, size);
 float* d_C; cudaMalloc(&d_C, size);
 cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
 cudaMemcpy(d_B, h_B, size, cudaMemcpyHostToDevice);

 VecAdd<<<blocksPerGrid, threadsPerBlock>>>(d_A, d_B, d_C, N);

 // Ahora, de vuelta a copiar a host memory (CPU).
 cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);
 verifyResults(h_C, size);

 cudaFree(d_A);
 cudaFree(d_B);
 cudaFree(d_C);
            
 // Free host memory
 ...
}
```


## Pipeline de gráficos

<img src='images/d3d11-pipeline-stages.jpg' height='440' />

Notas:
- Rápida reintroducción del pipeline


## Swap chains

<svg viewBox="0 0 400 200" xmlns="http://www.w3.org/2000/svg">
 <use xlink:href='images/swapchains.svg#svg8'></use>
</svg>

Notas:
- Grupo de buffers para mostrar en video
- Se encarga de coordinar con el display
- Al momento de mostrar, instantáneamente cambia la siguiente imagen (swap pointer)
- Más real en el caso de pantalla completa (accesso exclusivo) o consola
- Con compositor, engañapichanga
- El "Present" de swap chain hace flipping (noción de video) o copia (para componer en ventana)
- Antes de D3D12, el modelo de objetos permite usar siempre el "back buffer" y hacer flip


## Swap chain buffer count

- Single Buffer
- Double Buffer
- VSync
- Triple Buffer

Notas:
- "Single buffer" - no está bien soportado, muy viejo, implica tearing o hacer render en un momento particular, tipo DOS
- Double buffer - swap, pero necesita vsync para que la lectura sea correcta, si no - tearing
- VSync - cuando se terminó de hacer rendering, pero implica el refresh rate del monitor como medida "estándar"
- es decir: 60fps en el caso común, pero si no llega a un frame por refresh, tiene que cada dos, 30fps
- Triple buffer - no hace tears, y permite que siempre se haga trabajo (en double buffer, una vez que se terminó un frame, hay que esperar a que el front se haga disponible)


## Tearing

<img src='images/tearing.jpg' height='440' />


## Tearing

<img src="images/time.double.png" height='440' />

Notas:
- Usamos swap, pero sin vsync, podemos pifiera.


## VSync

<img src="images/time.vsync.png" height='440' />

Notas:
- Usamos swap y vsync, no la imagen que aparece es lejos de lo que estamos renderando.


## Triple

<img src="images/time.triple.png" height='440' />

Notas:
- Con triple buffering, podemos trabajar, renderear, y tener imagenes recientes.


## FreeSync y G-Sync

- FreeSync es el de AMD, G-Sync el de NVidia
- Necesita que el display se la banque (G-Sync pide royalties, FreeSync no)
- Otros variable refresh rate: VESA Adaptive-Sync, HDMI 2.1 VRR, Apple ProMotion en iPads

Notas:
- En vez del display marcando el reloj, el proveedor de contenido marca el paso de frames
- Tiene que reportar en reloj, pero puede introducir delays, con lo cual no hace falta esperar ciclos enteros
- Coordinación entre placa y monitor, no hace falta cambios programables (entonces: predicción por resultados)


## Pipeline de gráficos en DirectX (setup)

```C++
// Obtener device, context, swapchain
D3D11CreateDevice( nullptr, g_driverType, nullptr,
  createDeviceFlags, featureLevels, numFeatureLevels, 
  D3D11_SDK_VERSION, &g_pd3dDevice, &g_featureLevel,
  &g_pImmediateContext ); 
GetAdapterThenFactoryFromDevice(g_pd3dDevice, &pFactory);

DXGI_SWAP_CHAIN_DESC1 sd;
// Set: Width, Height, pixel format, samples, buffer usage (render target output), output window
pFactory->CreateSwapChain( g_pd3dDevice, &sd, &g_pSwapChain ); 

// Preparar un view para el render target
g_pSwapChain->GetBuffer( 0, __uuidof( ID3D11Texture2D ), reinterpret_cast<void**>( &pBackBuffer ) ); 
pd3dDevice->CreateRenderTargetView( pBackBuffer, nullptr, &g_pRenderTargetView ); 
g_pImmediateContext->OMSetRenderTargets( 1, &g_pRenderTargetView, nullptr ); 

D3D11_VIEWPORT vp;
// Set: Width, Height, min/max depth, top coordinates
g_pImmediateContext->RSSetViewports( 1, &vp );
```


## Pipeline de gráficos en DirectX (setup)

```C++
// En loop:
g_pImmediateContext->ClearRenderTargetView( g_pRenderTargetView, Colors::MidnightBlue );
g_pSwapChain->Present( 0, 0 );
```


## Pipeline de gráficos en DirectX (render)

```C++
// Compilacion de texto a bytecode 
ID3DBlob* pVSBlob = nullptr; 
hr = CompileShaderFromFile( L"Tutorial02.fx", "VS", "vs_4_0", &pVSBlob ); 
if( FAILED( hr ) )  { 
 MessageBox( nullptr, L"No pudo compilar", L"Error", MB_OK ); 
 return hr; 
} 
 
// Compila el driver
hr = g_pd3dDevice->CreateVertexShader( pVSBlob->GetBufferPointer(), pVSBlob->GetBufferSize(), nullptr, &g_pVertexShader ); 
if( FAILED( hr ) ) {
 pVSBlob->Release(); 
 return hr; 
} 
```


## Pipeline de gráficos en DirectX (render)

```C++
// Input layout - vertices
D3D11_INPUT_ELEMENT_DESC layout[] = {
 { "POSITION", 0, DXGI_FORMAT_R32G32B32_FLOAT, 0, 0, D3D11_INPUT_PER_VERTEX_DATA, 0 }, 
}; 
UINT numElements = ARRAYSIZE( layout ); 
 
// Create the input layout 
hr = g_pd3dDevice->CreateInputLayout( layout, numElements, pVSBlob->GetBufferPointer(),
 pVSBlob->GetBufferSize(), &g_pVertexLayout ); 
pVSBlob->Release(); 
if( FAILED( hr ) ) 
  return hr; 
 
// Set the input layout 
g_pImmediateContext->IASetInputLayout( g_pVertexLayout ); 
```


## Pipeline de gráficos en DirectX (render)

```C++
ID3DBlob* pPSBlob = ...; 
hr = g_pd3dDevice->CreatePixelShader( pPSBlob->GetBufferPointer(), pPSBlob->GetBufferSize(), nullptr, &g_pPixelShader ); 
pPSBlob->Release(); 
if( FAILED( hr ) ) 
 return hr; 
 
// Create vertex buffer 
SimpleVertex vertices[] = {
 XMFLOAT3( 0.0f, 0.5f, 0.5f ), 
 XMFLOAT3( 0.5f, -0.5f, 0.5f ), 
 XMFLOAT3( -0.5f, -0.5f, 0.5f ), 
}; 

D3D11_BUFFER_DESC bd; 
ZeroMemory( &bd, sizeof(bd) ); 
bd.Usage = D3D11_USAGE_DEFAULT; 
bd.ByteWidth = sizeof( SimpleVertex ) * 3; 
bd.BindFlags = D3D11_BIND_VERTEX_BUFFER; 
bd.CPUAccessFlags = 0; 
D3D11_SUBRESOURCE_DATA InitData; 
ZeroMemory( &InitData, sizeof(InitData) ); 
InitData.pSysMem = vertices; 
hr = g_pd3dDevice->CreateBuffer( &bd, &InitData, &g_pVertexBuffer ); 
if( FAILED( hr ) ) 
 return hr; 
```


## Pipeline de gráficos en DirectX (render)

```C++
// En loop.

// Color de fondo.
g_pImmediateContext->ClearRenderTargetView( g_pRenderTargetView, Colors::MidnightBlue ); 
 
// Estado de pipeline, shaders, y a trabajar.
UINT stride = sizeof( SimpleVertex ); 
UINT offset = 0; 
g_pImmediateContext->IASetVertexBuffers( 0, 1, &g_pVertexBuffer, &stride, &offset ); 

g_pImmediateContext->IASetPrimitiveTopology( D3D11_PRIMITIVE_TOPOLOGY_TRIANGLELIST ); 

g_pImmediateContext->VSSetShader( g_pVertexShader, nullptr, 0 );
g_pImmediateContext->PSSetShader( g_pPixelShader, nullptr, 0 );
g_pImmediateContext->Draw( 3, 0 );

// Presenta del back buffer al front buffer (ventana o pantalla)
g_pSwapChain->Present( 0, 0 );
```


## Perspectiva de trabajo

- "De a uno"
- Un thread (CS)
- Un vértice (VS)
- Un triángulo (GS)
- Un pixel (PS)

Notas:
- Difícil de cruzar estado - concurrencia


## Flujo de control en shaders

- Estructurado, no se permite goto.
- Sin excepciones.
- Sin llamadas virtuales (excepto engañapichanga).
- Sin stack (excepto engañapichanga).


## Valores uniformes y variables

- Hay datos que no varían de un thread a otro
- Por ejemplo, la posición de la cámara en el espacio es constante
- Si no hubiera valores variables, no sería muy útil


## Recursos y referencias ("naming")

- Limitaciones de hardware.
- Muy costoso reprogramas ciertas partes del sampler.

```C++
Texture2D t = (cond) ? t0 : t1;
t.Sample(...); <-- boom!
```

Notas:
- No está permitido utilizar recursos como variables.
- CUDA permite (un poco) con punteros.

Referencias: https://docs.nvidia.com/cuda/cuda-c-programming-guide/


# Preguntas

