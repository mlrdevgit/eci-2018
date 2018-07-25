#if 0
fxc BasicShaders.hlsl /E ps_main /T ps_4_0 /Od /Zi /Fh BasicShaders.ps.h
fxc BasicShaders.hlsl /E vs_main /T vs_4_0 /Od /Zi /Fh BasicShaders.vs.h
#endif

cbuffer transforms : register(b0) {
  float4x4 World;
  float4x4 View;
  float4x4 Projection;
};

struct ps_input {
  float4 pos : SV_POSITION;
  float4 color : COLOR;
};

ps_input vs_main(float4 pos : POSITION, float4 Color : COLOR) {
  ps_input p;

  pos = mul(pos, World);
  pos = mul(pos, View);
  pos = mul(pos, Projection);
  p.pos = pos;
  p.color = Color;
  return p;
}

float4 ps_main(ps_input input) : SV_Target {
  return input.color;
}
