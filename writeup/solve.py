sus = "& D 6 B P 0 e 9 o q d 8 O g 4 Q a A p R b"

flag = """2wF){c:"}Vc/E/}^(jL"_T.n52!My+D442{?k,JX)).llw.<(Fxm73]YX?i:^JW{!2kY[rZC3,z=)lj3]]nt+)Y>K}U"kXMl=f,-m{Zw75y)mNx5_2L}UF;,'HsIGrIEkiLU-H!vZ3SJ}_[_Vmz5v>Uc_iX3U9QbNE3
qDRq0&E4FNn}<UT-dbL3K,p608v*fq,(K5t&OAAXGpo4dQd<d0g8eH:AqeaR7OGBq6bDa:Qn&OgaqdTPO68g.y}7VX)FKF.RqQb3yO8bqDNRRQ&R0nIB80QWXh8Aaa[z>J[VX)'La&PRe+;A&0AD}_N46&6yk+;LOjX
o?VH^<*QlL."5NyO*XQu*RK{m^Du]AVk.^oS<)TgSQ(}kc5KoJL2*dKy=biK:gMQIT1i}!6K6)="J"m4lj/VeFIIK}m<s+qS1;I5T:y9US-6mr[FKH9KESmB10{Ur=OC[7Mfl?vjg3S*59]6[s:>Q.ai([s0)LZ.&-7
Bda4A;:&V<.WN]&I-Tlp>A_!H_/rq8/NM+a}(5?cyB06DB_:8UrZVdmK{DZzZphPBbg8HJPnq844g)tAUG<zp=>WNZyL>/!6ab&hr7jQc.79R&b41.43G:2c=6HFYI0<S*[C?sZYAk")Lo>gvZ^MAWeN:ZI8Vc)748_
&^[Yj'/Ax3vsjNR6AaB4^PMwbg8kxRmn)Fo:<!(7[&'J;F<'Pgg6d");2a+Vk8.4HX*.,'ako<'7M(XgmshX6!'j7MEizF,y37.RuTNQ]WL8H?l)NXp/]b9Pid7zZ'RIYV/[W.3Coq&OaHj94ao8r[AGy"k4[mzG4r(
anLvN^VAy1mFv?pmlW!DVA)TCN4E/q,zmE4]cLE63RisET]xQLITa>-s)9L.JQ"emG3!.WO<8'w/FW!8m<X=4l}VrECt)26L.T>d^Z_gJY!8N}K<S!QuF<2050s53HAlfG;JfUKw&TjZ^fjq5>U9Zyp2Vm"d.7(F&"j
D^+{jGIgOqeA9:qTKGS9nE9eO07w2)A0BGv8e4R:lAb9oeoy0{Lm-b>*EA?W3QzA7l":M=aMAdd8OOk&RaDQZX_Ww+yUILrdDQR)lNtp;1L0o&DPez(P0gBXhJa&De:W+f{E)N-L8iCJ<*!0zs-iby.POAD23e4Q'MT
N'^lfjvUXNWIGILY.2C?K>T>usSH_*2H<^'>5*N!ff):KNUhl(_<luLz'X}NS3tLK[F}Fy;<N[El;t;xT'NhXjOqBo64bY3Sm,MfC7c/"GxXIH=2;1cM[U?lKxuM?'xs8DB&qbeW:[l5t=lH-Ts}E7fV5K/3sw]<VYz"""

# only print out the char if its sus
for char in flag:
    if char == "\n":
        print()
    elif char in sus:
        print(char, end="")
    else:
        print(" ", end="")