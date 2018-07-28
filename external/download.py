import os
import os.path
import requests
import shutil

# otras dependencies para proceso de video:
# choco install ffmpeg
# pip install requests
# pip install pytube
# pip install moviepy

target_dir = os.path.dirname(os.path.abspath(__file__))

downloads = [
    ("escenas-mgs-suciedad.jpg", "http://www.adriancourreges.com/img/blog/2017/mgsv/40_dirt_after.jpg"),
    ("escenas-mgs-profundidad.jpg", "http://www.adriancourreges.com/img/blog/2017/mgsv/35_dof_compose.png"),
    ("escenas-mgs-particulas.jpg", "http://www.adriancourreges.com/img/blog/2017/mgsv/23_particles_3.jpg"),
    ("escenas-mgs-ssr.jpg", "http://www.adriancourreges.com/img/blog/2017/mgsv/20_ssr_color.jpg"),
    ("escenas-mgs-trans.jpg", "http://www.adriancourreges.com/img/blog/2017/mgsv/18_transparent.jpg"),
    ("escenas-mgs-luces-2.jpg", "http://www.adriancourreges.com/img/blog/2017/mgsv/14_shadow_diffuse_4.jpg"),
    ("escenas-mgs-shadow-maps.jpg", "http://www.adriancourreges.com/img/blog/2017/mgsv/13_shadowmap.jpg"),
    ("escenas-mgs-luces-1.jpg", "http://www.adriancourreges.com/img/blog/2017/mgsv/12_nonshadow_diffuse_4.jpg"),
    ("escenas-mgs-gi.jpg", "http://www.adriancourreges.com/img/blog/2017/mgsv/10_sh_diffuse_4.jpg"),
    ("escenas-mgs-ssao.jpg", "http://www.adriancourreges.com/img/blog/2017/mgsv/08_ssao.jpg"),
    ("escenas-mgs-vels.jpg", "http://www.adriancourreges.com/img/blog/2017/mgsv/05_velocity_fin.jpg"),
    ("escenas-mgs-vel.png", "http://www.adriancourreges.com/img/blog/2017/mgsv/05_velocity_dyn.png"),
    ("escenas-mgs-gbuffer.png", "http://www.adriancourreges.com/img/blog/2017/mgsv/04_gbuffer_format.png"),
    ("escenas-piso.jpg", "http://www.adriancourreges.com/img/blog/2017/mgsv/02_depth_pp_3.jpg"),
    ("escenas-heightmap.jpg", "http://www.adriancourreges.com/img/blog/2017/mgsv/01_heightmap.jpg"),
    ("escenas-mgs.jpg", "http://www.adriancourreges.com/img/blog/2017/mgsv/99_final.jpg"),
    ("escenas-forward-plus.jpg", "https://www.3dgep.com/wp-content/uploads/2015/08/Forward-.jpg"),
    ("escenas-deferred-buffers.png", "https://cdn.tutsplus.com/gamedev/uploads/2013/10/buffers.png"),
    ("escenas-deferred.png", "https://cdn.tutsplus.com/gamedev/uploads/2013/11/deferred-v2.png"),
    ("escenas-forward.png", "https://cdn.tutsplus.com/gamedev/uploads/2013/11/forward-v2.png"),
    ("barrel.jpg", "https://actioncamguides.com/wp-content/uploads/2017/05/epaperpress.jpg"),
    ("pincushion.jpg", "https://sjcam.com/wp-content/uploads/2017/09/Distortion-Correction-1-1024x808.jpg"),
    ("fisheye.png", "https://www.khaolakexplorer.com/similan-islands-liveaboard/wp-content/uploads/2016/08/fish-eye-vs-rectilinear.jpg"),
    ("projection-transform.png", "https://docs.microsoft.com/en-us/windows/desktop/direct3d9/images/cuboid.png"),
    ("view-transform.png", "https://msdn.microsoft.com/dynimg/IC412715.png"),
    ("world-transform.png", "https://msdn.microsoft.com/dynimg/IC412718.png"),
    ("escenas-forward.png", "https://cdn.tutsplus.com/gamedev/uploads/2013/11/forward-v2.png"),
    ("camaras-frustum.jpg", "https://upload.wikimedia.org/wikipedia/commons/3/30/ViewFrustum.jpg"),
    ("meshes-unreal-level.png", "https://docs.unrealengine.com/portals/0/images/Engine/LevelStreaming/Overview/PersistentLevel.png"),
    ("meshes-konigsberg.png", "https://upload.wikimedia.org/wikipedia/commons/5/5d/Konigsberg_bridges.png"),
    ("meshes-winged.jpg", "https://upload.wikimedia.org/wikipedia/commons/b/b7/Mesh_we2.jpg"),
    ("meshes-ff7-real.jpg", "http://i.imgur.com/oJJkl.jpg"),
    ("meshes-ff7.jpg", "https://www.technobuffalo.com/wp-content/uploads/2015/06/Final-Fantasy-VII1.jpg"),
    ("meshes-dolphin.png", "https://upload.wikimedia.org/wikipedia/commons/f/fb/Dolphin_triangle_mesh.png"),
    ("meshes-chichen-itza.jpg", "https://upload.wikimedia.org/wikipedia/commons/5/51/Chichen_Itza_3.jpg"),
    ("caffe2-operators-comparison.png", "https://caffe2.ai/static/images/operators-comparison.png"),
    ("frameworks-coremltrain.png", "https://docs-assets.developer.apple.com/published/692e733304/4eaa95da-421f-4812-8938-2bada720444e.png"),
    ("ml-canny.jpg", "https://docs.opencv.org/trunk/canny1.jpg"),
    ("ml-histograma-4.jpg", "https://docs.opencv.org/2.4/_images/Histogram_Equalization_Equalized_Histogram.jpg"),
    ("ml-histograma-3.jpg", "https://docs.opencv.org/2.4/_images/Histogram_Equalization_Equalized_Image.jpg"),
    ("ml-histograma-2.jpg", "https://docs.opencv.org/2.4/_images/Histogram_Equalization_Original_Histogram.jpg"),
    ("ml-histograma-1.jpg", "https://docs.opencv.org/2.4/_images/Histogram_Equalization_Original_Image.jpg"),
    ("ml-auto.png", "https://upload.wikimedia.org/wikipedia/commons/2/27/Sketchup_car_model.png"),
    ("hsl-hsv.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Hsl-hsv_models.svg/480px-Hsl-hsv_models.svg.png"),
    ("cmyk-separado.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/CMYK_separation_%E2%80%93_maximum_black.jpg/301px-CMYK_separation_%E2%80%93_maximum_black.jpg"),
    ("rgb-cubo.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/RGB_color_solid_cube.png/640px-RGB_color_solid_cube.png"),
    ("cie-temperatura.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/PlanckianLocus.png/427px-PlanckianLocus.png"),
    ("cie-1931-notas.gif", "http://hyperphysics.phy-astr.gsu.edu/hbase/vision/imgvis/colper.gif"),
    ("espacios-colores.png", "https://upload.wikimedia.org/wikipedia/commons/1/13/Color_solid_comparison_hsl_hsv_rgb_cone_sphere_cube_cylinder.png"),
    ("helmholtz.svg", "https://upload.wikimedia.org/wikipedia/commons/e/e6/Helmholtz-Kohlrausch_effect.svg"),
    ("cie-1931.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/CIExy1931.png/434px-CIExy1931.png"),
    ("cones-spectrum.svg", "https://upload.wikimedia.org/wikipedia/commons/0/04/Cone-fundamentals-with-srgb-spectrum.svg"),
    ("verde-rojo.png", "https://upload.wikimedia.org/wikipedia/commons/a/a7/Economic_Freedom_Charts.png"),
    ("goethe-rueda.jpg", "https://programmingdesignsystems.com/assets/color/a-short-history-of-color-theory/goethe-color-circle.jpg"),
    ("pescados.jpg", "https://c1.staticflickr.com/5/4132/5129962638_fa304fa22b_b.jpg"),
    ("motion-blur.jpg", "https://i2.wp.com/digital-photography-school.com/wp-content/uploads/2010/08/motion-blur-dance.jpg?resize=600&amp;ssl=1"),
    ("interlacing-malo.jpg", "https://upload.wikimedia.org/wikipedia/commons/1/19/Interlaced_video_frame_%28car_wheel%29.jpg"),
    ("animacion.gif", "https://upload.wikimedia.org/wikipedia/commons/0/0a/Man_on_a_Treadmill_GIF_Animation_Loop.gif"),
    ("scenekit-nodes.png", "https://docs-assets.developer.apple.com/published/4f035789b7/592d7da9-814c-4bbd-b1a7-0e07b3003d94.png"),
    ("rainier-lejos.jpg", "https://cdn.loc.gov/service/pnp/highsm/16400/16443v.jpg"),
    ("bajo-agua.jpg", "https://www.publicdomainpictures.net/pictures/10000/velka/1-1254411102IlVs.jpg"),
    ("scenekit-particles.png", "https://koenig-media.raywenderlich.com/uploads/2016/03/AddParticleSystem1.png"),
    ("minecraft-voxels.jpg", "https://community-content-assets.minecraft.net/upload/styles/small/s3/b19c86ed0dcd8614b82fd84592d1db69-ingame.jpg"),
    ("skybox.png", "https://upload.wikimedia.org/wikipedia/commons/b/b4/Skybox_example.png"),
    ("xbox-one-gpu.jpg", "https://www.techpowerup.com/gpudb/images/c754_X871363-001.jpg"),
    ("comanche.jpg", "https://www.rockpapershotgun.com/images/10/mar/comanche.jpg/RPSS/resize/760x-1/format/jpg/quality/70"),
    ("spline.png", "https://upload.wikimedia.org/wikipedia/commons/f/fd/Spline_%28PSF%29.png"),
    ("newton-raphson.gif", "http://web.mit.edu/10.001/Web/Course_Notes/NLAE/figure17_2.gif"),
    ("camara-chromatic-focus.jpg", "https://cdn.photographylife.com/wp-content/uploads/2011/04/Focus-Accuracy-AF-Fine-Tune-2.jpg"),
    ("camara-chromatic-aberration.png", "https://cdn.photographylife.com/wp-content/uploads/2011/10/Longitudinal-Chromatic-Aberration.png"),
    ("camara-interna.png", "https://cdn.photographylife.com/wp-content/uploads/2017/03/DSLR-Compared-to-Mirrorless-Camera.png"),
    ("luz-interferencia-color.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Dieselrainbow.jpg/538px-Dieselrainbow.jpg"),
    ("luz-interferencia.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Optical_flat_interference.svg/573px-Optical_flat_interference.svg.png"),
    ("espectro-lamparitas.png", "http://justinmklam.com/imgs/blog-imgs/sad-lamp/spectral_responses2.png"),
    ("fluorescent.jpg", "https://cdn.pixabay.com/photo/2016/01/16/01/59/fluorescent-1142762_1280.jpg"),
    ("float.svg", "https://upload.wikimedia.org/wikipedia/commons/d/d2/Float_example.svg"),
    ("wolf3d.jpg", "https://lodev.org/cgtutor/images/wolf3d.jpg"),
    ("acne-large.png", "http://www.opengl-tutorial.org/assets/images/tuto-16-shadow-mapping/1rstTry.png"),
    ("acne-bias.png", "http://www.opengl-tutorial.org/assets/images/tuto-16-shadow-mapping/FixedBias.png"),
    ("shading-modes.png", "https://upload.wikimedia.org/wikipedia/commons/6/62/D3D_Shading_Modes.png"),
    ("gpu-memory.jpg", "http://www.farbrausch.de/~fg/gpu/gpu_memory.jpg"),
    ("anisotropic.png", "https://upload.wikimedia.org/wikipedia/commons/8/80/Anisotropic_filtering_en.png"),
    ("ogre-fresnel.jpg", "https://cms-assets.tutsplus.com/uploads/users/218/posts/21469/image/ogre-fresnel.jpg"),
    ("amd-fusion-2011.pdf", "http://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15869-f11/www/lectures/mantor_AMD_CMU_10_2011.pdf"),
    ("mobile-adreno-opencl-opt.pdf", "https://developer.qualcomm.com/qfile/33472/80-nb295-11_a.pdf"),
    ("perf-sol-ratios.png", "https://devblogs.nvidia.com/wp-content/uploads/2018/01/SOL-Image-10.png"),
    ("perf-sol-registros.png", "https://devblogs.nvidia.com/wp-content/uploads/2018/02/SOL-Image-9_1_New-002.png"),
    ("perf-sol-ranking.png", "https://devblogs.nvidia.com/wp-content/uploads/2018/02/SOL-Image-7_New.png"),
    ("perf-sol-guia.png", "https://devblogs.nvidia.com/wp-content/uploads/2018/01/SOL-Image-6.png"),
    ("perf-gpu-memory.png", "https://msdnshared.blob.core.windows.net/media/2017/11/gpumemory.png"),
    ("perf-timing-capture.png", "https://msdnshared.blob.core.windows.net/media/2016/11/timingcapture.png"),
    ("perf-loop.png", "https://docs-assets.developer.apple.com/published/beef028d16/1b2e406d-c49e-4d11-9888-850579f5f8ab.png"),
    ("perf-objetivos.jpg", "http://www.ingeniovirtual.com/wp-content/uploads/Definicion-de-objetivos-en-el-marketing-online.jpg"),
    ("perf-wpa-sample.png", "https://msdnshared.blob.core.windows.net/media/TNBlogsFS/prod.evol.blogs.technet.com/CommunityServer.Blogs.Components.WeblogFiles/00/00/00/52/09/metablogapi/6136.image_4FF4CD3F.png"),
    ("time.double.png", "https://images.anandtech.com/reviews/video/triplebuffer/time.double.png"),
    ("time.vsync.png", "https://images.anandtech.com/reviews/video/triplebuffer/time.vsync.png"),
    ("time.triple.png", "https://images.anandtech.com/reviews/video/triplebuffer/time.triple.png"),
    ("tearing.jpg", "https://i.ytimg.com/vi/bpny_V_VTWU/maxresdefault.jpg"),
    ("conexion-memoria.png", "https://mynameismjp.files.wordpress.com/2018/01/amd_caches.png?w=756"),
    ("sgemm-perf.png", "https://cnugteren.github.io/tutorial/images/performance0.png"),
    ("pcie.jpg", "https://lh3.googleusercontent.com/kHIhvPLh8flyn2fr9uurUz0tzjQpu9sjIqGCrabWWM53pwQZ1JFnAV4SYEeI55fJ18AbdvyypVOAx_o8gGUTQ3lmGPxGZLEgPGYGAqhEO_q9tD9AX1f3uo22xCSvFEWuu-n2NvPXu9amHj4CJQlwJ1lWVsw-XLNh8mDexSLyO-VhQ3axbhqmK0ftt-Vpa37UvBnKmJeysZJXMbsZ8F-q7zgdo16gUURH3-9e2ATIjvk4Um9Dg-mBh4_b4a2ODcOYZ-Sj7qL1vqUUcuJP9MfUQV-EY3qxwnLCkMfVRd97ugVKo35cMexdwV0JWUvsjHJTZCtlxQ4UneXTLcvRHe28XkUqZSvpeLS3_JPyLJVnkOziCwL1lBwnXwhFYMJGWRz0WLFN3oelRQ-lPaaTjZs3xr4W8037mVoPZonCBRPi2FOe_zEJSyvxeDiDqLbp2WuGnX5xAPONNTNgcKLMtH8vD30O-W9efR52u_E21DSZWABALEbzQ1Kzf32jcZRvGELTUPySd6cv2Yzn4F-kXWDP3tYuy1oRsPvvq_RJPhMVxSpfzgKG3IEH9N6Kprx0ch8-5PZK-eMTYN2sUB6GUC982RkdqQz1BP7vz1Jc5vESiI1vFZkoL3g_=w800-h485-no"),
    
    ("gimbal-lock.png", "https://upload.wikimedia.org/wikipedia/commons/3/38/Gimbal_lock.png"),
    ("plane-axis.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Yaw_Axis_Corrected.svg/709px-Yaw_Axis_Corrected.svg.png"),
    ("aperture-blades.png", "https://docs-assets.developer.apple.com/published/250b5e0969/755e7ad0-b0b9-4c2f-8e3e-6b5bdeabcabe.png"),
    ("camera.png", "https://docs-assets.developer.apple.com/published/c930c799fe/1f516915-005c-4949-9bc9-38a3fe9f2a7d.png"),
    ("scenekit.png", "https://docs-assets.developer.apple.com/published/4f035789b7/592d7da9-814c-4bbd-b1a7-0e07b3003d94.png"),
    ("transformers.jpg", "https://i.ytimg.com/vi/JZzlnbcfnhA/hqdefault.jpg"),
    ("transportador-r.svg.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/TransportadorR.svg/300px-TransportadorR.svg.png"),
    ("transportador-g.svg.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/TransportadorG.svg/300px-TransportadorG.svg.png"),
    ("trigonometria-plot.svg.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Funci%C3%B3n_Trigonom%C3%A9trica_R111.svg/740px-Funci%C3%B3n_Trigonom%C3%A9trica_R111.svg.png"),
    ("cross-product-components.gif", "https://www.mathsisfun.com/algebra/images/cross-product-components.gif"),
    ("cross-product-angle.gif", "https://www.mathsisfun.com/algebra/images/cross-product.gif"),
    ("vertical-illusion.png", "https://upload.wikimedia.org/wikipedia/commons/3/30/Vertical%E2%80%93horizontal_illusion.png"),
    ("grey-square-illusion-1.gif", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Grey_square_optical_illusion.svg/764px-Grey_square_optical_illusion.svg.png"),
    ("grey-square-illusion-2.gif", "https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/Grey_square_optical_illusion_proof2.svg/764px-Grey_square_optical_illusion_proof2.svg.png"),
    ("gradient-illusion.svg.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Gradient-optical-illusion.svg/1024px-Gradient-optical-illusion.svg.png"),
    ("rcdist.gif", "http://hyperphysics.phy-astr.gsu.edu/hbasees/vision/imgvis/rcdist.gif"),
    ("eyesection.svg", "https://upload.wikimedia.org/wikipedia/commons/b/ba/Eyesection-es.svg"),
    ("retinografia.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Retinography.jpg/1024px-Retinography.jpg"),
    ("ojo-interno.png", "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Three_Internal_chambers_of_the_Eye_esp.png/880px-Three_Internal_chambers_of_the_Eye_esp.png"),
    ("d3d11-pipeline-stages.jpg", "https://docs.microsoft.com/en-us/windows/desktop/direct3d11/images/d3d11-pipeline-stages.jpg"),
    ("d3d10-rasterrulestriangle.png", "https://docs.microsoft.com/en-us/windows/desktop/direct3d11/images/d3d10-rasterrulestriangle.png"),
    ("tess-prog.png", "https://docs.microsoft.com/en-us/windows/desktop/direct3d11/images/tess-prog.png"),
    ("d3d11-hull-shader.png", "https://docs.microsoft.com/en-us/windows/desktop/direct3d11/images/d3d11-hull-shader.png"),
    ("d3d11-domain-shader.png", "https://docs.microsoft.com/en-us/windows/desktop/direct3d11/images/d3d11-domain-shader.png"),
    ("model-comparison.jpg", "http://www.nvidia.com/docs/IO/91797/model_comparision.jpg"),
    ("d3d11-gsinputs2.png", "https://docs.microsoft.com/en-us/windows/desktop/direct3dhlsl/images/d3d11-gsinputs2.png"),

    ("intel-gen9.pdf", "https://software.intel.com/sites/default/files/managed/c5/9a/The-Compute-Architecture-of-Intel-Processor-Graphics-Gen9-v1d0.pdf"),

    ("amd-gcn3.pdf", "http://32ipi028l5q82yhj72224m8j-wpengine.netdna-ssl.com/wp-content/uploads/2016/08/AMD_GCN3_Instruction_Set_Architecture_rev1.1.pdf")

    ]

# video_clips: url, local_name, clip_name, start_time (seconds), end_time (seconds)
video_clips = [
    ("https://www.youtube.com/watch?v=mfRvCSBD4q0", "wing-commander", "billboard", 300, 330),
    ("https://www.youtube.com/watch?v=TGJ0yzNR0xA", "skyrim-popping", "poor", 70, 105),
    ("https://www.youtube.com/watch?v=shT0Y160qP4", "witcher-sky", "anim", 300, 320),
    ("https://www.youtube.com/watch?v=fem3ZQ1sCO0", "comanche", "altura", 60, 85),
    ("https://www.youtube.com/watch?v=kH_UPUvTuRQ", "unity-worldcomposer", "altura", 780, 840),
    ("https://www.youtube.com/watch?v=ptm_sH1zK7Y", "gow4-chainsaw", "", 0, 0),
    ("https://www.youtube.com/watch?v=EWfJguFckrE", "skyrim-spells", "", 0, 0),
    ("https://www.youtube.com/watch?v=sSB4QcQMm6E", "alan-wake-trailer", "", 0, 0),
    ("https://www.youtube.com/watch?v=e0W65ScZmQw", "doom-bsp", "traverse", 80, 140),
    ("https://www.youtube.com/watch?v=Js5JpabUO28", "titanic-hand", "", 0, 0),
    ("https://www.youtube.com/watch?v=jt8xRaZkxwE", "sea-thieves", "ball", 940, 880),
    ("https://www.youtube.com/watch?v=fbfaBJ4nOBI", "warcraft", "walk", 30, 48),
    ("https://www.youtube.com/watch?v=HdfAzUXvmOQ", "piano-mover", "first", 50, 80),
    ("https://www.youtube.com/watch?v=eDk4HrEtGrM", "saccadic-redirection", "", 0, 0),
    ("https://www.youtube.com/watch?v=snSbguhHCic", "rise-tr", "adaptacion", 1310, 1370),
    ("https://www.youtube.com/watch?v=KieoxDq4Xak", "simplygon-remeshing", "", 0, 0),
    ("https://www.youtube.com/watch?v=Zq5mrApE98A", "mgs-buffers", "", 0, 0)
    ]

def download_clip(url, local_name, local_name_clip, start_time, end_time):
    full_local_path = os.path.join(target_dir, local_name + ".mp4")
    if not os.path.exists(full_local_path):
        from pytube import YouTube
        print("downloading " + local_name)
        yt = YouTube(url).streams.filter(progressive=True, file_extension='mp4').first()
        full_local_path = os.path.join(target_dir, local_name + "." + yt.subtype)
        if not os.path.exists(full_local_path):
            yt.download(target_dir, local_name)
        else:
            print("already exists with extension ." + yt.subtype)
    if start_time != end_time:
        if not os.path.exists(local_name_clip + ".mp4"):
            print("extracting to " + local_name_clip)
            from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
            ffmpeg_extract_subclip(full_local_path, start_time, end_time, targetname=local_name_clip + ".mp4")

def download_files():
    for a, url in downloads:
        target_file = os.path.join(target_dir, a)
        if not os.path.exists(target_file):
            print("downloading " + url + " into " + target_file) 
            response = requests.get(url, stream=True)
            with open(target_file, 'wb') as out_file:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, out_file)
            del response

def download_clips():
    for url, local_name, clip_name, start_time, end_time in video_clips:
        local_name_clip = local_name + "-" + clip_name
        download_clip(url, local_name, local_name_clip, start_time, end_time)

def run():
    download_files()
    download_clips()

if __name__ == "__main__":
    run()
