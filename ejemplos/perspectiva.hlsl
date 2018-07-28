// -*- mode: hlsl; hlsl-entry: VSMain; hlsl-target: vs_5_0; hlsl-args: /Zi; -*-

struct PSInput {
 float4 position : SV_POSITION;
 float4 color : COLOR;
};

static const float PI = 3.14159265f;

// world: empujamos los triangulos para atras.
static float4x4 world = {
 { 1, 0, 0, 0 },
 { 0, 1, 0, 0 },
 { 0, 0, 1, 0 },
 { 0, 0, 4, 1 }
};

// una matrix identidad, dejamos la camara en el origen
static float4x4 view = {
 { 1, 0, 0, 0 },
 { 0, 1, 0, 0 },
 { 0, 0, 1, 0 },
 { 0, 0, 0, 1 }
};

// cambio de fov
static float fov_w = PI*0.5; // ~90 grados, en radianes
static float fov_h = PI*0.5;
static float w = 1/tan(fov_w/2);
static float h = 1/tan(fov_h/2);
static float Znear = 0;
static float Zfar = 100;
static float Q = Zfar / (Zfar - Znear);

static float4x4 projection = {
 { w, 0, 0, 0 },
 { 0, h, 0, 0 },
 { 0, 0, Q, 1 },
 { 0, 0, -Q * Znear, 0 }
};

float4x4 scale(float factor) {
 float4x4 result = {
  { factor, 0, 0, 0 },
  { 0, factor, 0, 0 },
  { 0, 0, factor, 0 },
  { 0, 0, 0, 1}
 };
 return result;
}

float4x4 transform3(float x, float y, float z) {
 float4x4 result = {
  { 1, 0, 0, 0 },
  { 0, 1, 0, 0 },
  { 0, 0, 1, 0 },
  { x, y, z, 1 }
 };
 return result;
}

PSInput VSMain(float4 position: POSITION, float4 color: COLOR) {
 float4 p = position;
 p = mul(p, scale(10));  // agrandamos el triangulo original
 p = mul(p, world);      // lo ponemos en el mundo
 p = mul(p, view);       // ajustamos para poner en referencia a la camara
 p = mul(p, projection); // proyectamos

 PSInput result;
 result.position = p;
 result.color = color;
#if visualizacion_x
 p.xyz /= p.w; p.w = 1; // normalizo por w ("no importa")
 result.color.rgb = (p.x + 1) / 2; // ajusto para el rango -1 a 1
 result.color.a = 1;
#endif
 return result;
}
float4 PSMain(PSInput input) : SV_TARGET {
 return input.color;
}

#if SHADER_OP_XML
<ShaderOp PS='PS' VS='VS'>
 <RootSignature>RootFlags(ALLOW_INPUT_ASSEMBLER_INPUT_LAYOUT)</RootSignature>
 <Resource Name='VBuffer' Dimension='BUFFER' Width='1024' Flags='ALLOW_UNORDERED_ACCESS' InitialResourceState='COPY_DEST' Init='FromBytes'>
  { {   0.0f,  0.25f , 0.0f }, { 1.0f, 0.0f, 0.0f, 1.0f } },
  { {  0.25f, -0.25f , 0.0f }, { 0.0f, 1.0f, 0.0f, 1.0f } },
  { { -0.25f, -0.25f , 0.0f }, { 0.0f, 0.0f, 1.0f, 1.0f } }

  { {  0.25f, -0.25f , 0.0f }, { 0.0f, 1.0f, 0.0f, 1.0f } },
  { {   0.0f,  0.25f , 0.0f }, { 1.0f, 0.0f, 0.0f, 1.0f } },
  { {  0.50f,  0.25f , 0.5f }, { 1.0f, 0.0f, 0.0f, 1.0f } },
 </Resource>
 <DescriptorHeap Name='RtvHeap' NumDescriptors='1' Type='RTV'>
 </DescriptorHeap>
 <InputElements>
  <InputElement SemanticName='POSITION' Format='R32G32B32_FLOAT' AlignedByteOffset='0' />
  <InputElement SemanticName='COLOR' Format='R32G32B32A32_FLOAT' AlignedByteOffset='12' />
 </InputElements>
 <Shader Name='VS' Target='vs_5_0' EntryPoint='VSMain' />
 <Shader Name='PS' Target='ps_5_0' EntryPoint='PSMain' />
</ShaderOp>
#endif
