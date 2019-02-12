import scipy.io as scio
import numpy as np
from pyh import *
import xml.etree.ElementTree as ET
import collections
# xml = ET.parse('XML.xml')
class tenseg_skeleton(object):

    def __init__(self,data_name):
        self.mem = {}
        self.bar_mem = collections.defaultdict(set)
        self.p2end = {}
        self.data = scio.loadmat(data_name)
        self.Cb = self.data['C_b']
        self.Cs = self.data['C_s']
        self.N = self.data['N']
        self.worldbody = worldbody()
        Geom = geom(name="floor",pos="0 0 -10",size="0 0 1",type="plane",material="matplane")
        Light = light(directional="true",diffuse=".8 .8 .8",specular=".2 .2 .2",pos="0 0 5",dir="0 0 -1")
        Site = site(name="s0",pos="0 0 0",size="0.1")
        Body = body(name = 'floor',pos = '0 0 0')
        Body<<Geom
        Body<<Light
        Body<<Site
        self.worldbody<<Body
        self.strcounter = 1
        self.front = '''<mujoco model="dbar">

    <option timestep="0.01" iterations="50" solver="Newton" tolerance="1e-10" gravity = "0 0 0" collision="predefined" viscosity=".5"/>

    <size njmax="5000" nconmax="1000" nstack="20000"/>

    <visual>
        <rgba haze=".3 .3 .3 1"/>
    </visual>

    <default>
        <position ctrllimited="false" ctrlrange="-1 1" gear="1.0"/>
        <tendon damping="2" rgba = ".8 .8 .8 .5"/>
        <geom size="0.01"/>
        <site size="0.01"/>
    </default>

    <asset>
        <texture type="skybox" builtin="gradient" rgb1="0.6 0.6 0.6" rgb2="0 0 0" width="512" height="512"/> 

        <texture name="texplane" type="2d" builtin="checker" rgb1=".25 .25 .25" rgb2=".3 .3 .3" width="512" height="512" mark="cross" markrgb=".8 .8 .8"/>  

        <material name="matplane" reflectance="0.3" texture="texplane" texrepeat="1 1" texuniform="true"/>
    </asset>'''
        self.rem = '''</mujoco>'''
        # print(str(self.N[0])[1:-1])
    def _addstr(self):
        S = np.dot(self.N.T,self.Cs.T)
        ns = len(S[0])
        s = S.T
        Tendon = tendon()
        for i in range(ns):
            strstart = str(self.N[list(self.Cs[i]).index(-1)])[1:-1]
            strend = str(self.N[list(self.Cs[i]).index(1)])[1:-1]
            sname = self.mem[strstart]
            ename = self.mem[strend]
            tmps = spatial(name = 'S' + str(self.strcounter),width = '0.02')
            self.strcounter += 1
            ssite = site(site = sname)
            esite = site(site = ename)
            command1 = 'tmps<<ssite'
            command2 = 'tmps<<esite'
            command3 = 'Tendon<<tmps'
            eval(command1)
            eval(command2)
            eval(command3)

            wait = str(Tendon.render())
            n = len(wait)
            s = 0
            wait_list = []
            for i in range(n-1):
                if wait[i]=='>' and wait[i+1] == '<':
                    tmp = wait[s:i+1] + '''\n'''
                    s = i+1
                    wait_list.append(tmp)
            wait_list.append(wait[s:])
        return "\n" +  "".join(wait_list) 
            # tmps = spatial(name = 'S' + str(self.strcounter),width = '0.02')
            # self.strcounter += 1

    def _addbar(self):
        # print(self.Cb)
        site_set = set()
        site_counter = 0
        # self.N = np.array(round(list(self.N),4))
        resN = []
        for i in self.N:
            tmp = []
            for j in i:
                tmp.append(round(j,4))
            resN.append(tmp)
        self.N = np.array(resN)
        B = np.dot(self.N.T,self.Cb.T)
        # S = np.dot(self.N.T,self.Cs.T)
        # B = self.N.T * self.Cb.T
        n = len(B[0])
        # b = [[B[0][i],B[1][i],B[2][i]] for i in range(n)]
        b = B.T
        # print(self.N,self.Cb,B)
        # print(self.N.shape,self.Cb.shape,B.shape)





        for i in range(n):
            start = self.N[list(self.Cb[i]).index(-1)]
            globalend = str(self.N[list(self.Cb[i]).index(1)])[1:-1]
            # actend = 
            # print(start)
            pos = str(start)[1:-1]
            end = str(b[i])[1:-1]
            # etest = end
            # ptest = pos
            # this part is for round in py
            # ss = pos.split(' ')
            # ee = end.split(' ')
            # st1 = []
            # st2 = []
            # for eee in ee:
            #     if eee:
            #         tmp = ''
            #         for le in eee:
            #             if le !=',':
            #                 tmp += le
            #         st1.append(round(float(tmp),4))
            # print(st1)
            # pos = ''
            # for posstr in st1:
            #     pos += ' ' + str(posstr)
            # for sss in ss:
            #     if sss:
            #         tmp = ''
            #         for le in sss:
            #             if le !=',':
            #                 tmp += le
            #         # sss = filter(',',sss)
            #         st2.append(round(float(tmp),4))
            # str2 = ' '
            # for tmpstr in st1:
            #     str2 += ' ' + str(tmpstr)

            # end = ""
            # for t in range(3):
            #     end += " " + str(round(st1[t]+st2[t],4))

            # to build body and it's child tag, joint geom and site
            bodyname = 'body' + str(i)
            self.bar_mem[str(start)[1:-1]].add(bodyname)
            self.bar_mem[globalend].add(bodyname)
            self.p2end[bodyname] = end

            locals()["Body"+str(i)] = body(name = "body"+str(i),pos=pos)
            tmpj = joint(type="free",pos="0 0 0")
            command = "Body"+str(i) + "<<tmpj"
            eval(command)
            tmpg = geom(name ="body"+str(i),type = "capsule",fromto="0 0 0 "+ end ,rgba=".5 .1 .1 1")
            command = "Body"+str(i) + "<<tmpg"
            eval(command)

            # for k in [pos,globalend]:
            # for k in ['0 0 0 ',end]:
            # if start not in 
                # globalk = pos + k
                # if k== '0 0 0 ':
            if str(start) not in site_set:
                site_set.add(str(start))
                site_name = 'site' + str(site_counter)
                self.mem[str(start)[1:-1]] = site_name
                site_pos = '0 0 0'
                tmps = site(name = site_name, pos = site_pos)
                site_counter += 1
                command = "Body" + str(i) + "<<tmps"
                eval(command)


            if globalend not in site_set:
                site_set.add(globalend)
                site_name = 'site' + str(site_counter)
                self.mem[str(globalend)] = site_name

                site_pos = end
                tmps = site(name = site_name, pos = site_pos)
                site_counter += 1
                command = "Body" + str(i) + "<<tmps"
                eval(command)


            command = "self.worldbody<<Body" + str(i)
            eval(command)

        wait = str(self.worldbody.render())
        n = len(wait)
        s = 0
        wait_list = []
        for i in range(n-1):
            if wait[i]=='>' and wait[i+1] == '<':
                tmp = wait[s:i+1] + '''\n'''
                s = i+1
                wait_list.append(tmp)
        wait_list.append(wait[s:])
        # wait_list = wait_list[1:]
        # wait_list[-1] = wait_list[-1][1:-14]

        # print(wait_list)
        # print("".join(wait_list))
        return self.front + "\n" +  "".join(wait_list) + "\n"
    def _addcon(self):
        equ = equality()
        ct = 1
        for i in self.bar_mem:
            if len(list(self.bar_mem[i]))>=2:
                s = list(self.bar_mem[i])[0]
                for j in list(self.bar_mem[i])[1:]:
                    tmpc = connect(active = 'true',name = s + '2' + j,body1 = s,body2 = j,anchor=self.p2end[s])
                    command = 'equ<<tmpc'
                    eval(command)


        wait = str(equ.render())
        n = len(wait)
        s = 0
        wait_list = []
        for i in range(n-1):
            if wait[i]=='>' and wait[i+1] == '<':
                tmp = wait[s:i+1] + '''\n'''
                s = i+1
                wait_list.append(tmp)
        wait_list.append(wait[s:])
        return "\n" +  "".join(wait_list) + "\n"
                    # tmpc = connect(activate = 'true',name = s + '2' + j,body1 = s,body2 = j,anchor='-0.05 0 0')
    def _addact(self,actuatorlist:'List' = []):
        if not actuatorlist:
            actuatorlist = range(1,self.strcounter)
        act = actuator()
        for i in actuatorlist:
            print(i)
            tmpp = position(tendon = 'S' + str(i),kp = '1')
            command = 'act<<tmpp'
            eval(command)
        wait = str(act.render())
        n = len(wait)
        s = 0
        wait_list = []
        for i in range(n-1):
            if wait[i]=='>' and wait[i+1] == '<':
                tmp = wait[s:i+1] + '''\n'''
                s = i+1
                wait_list.append(tmp)
        wait_list.append(wait[s:])
        return "\n" +  "".join(wait_list) + "\n" 
    def save_to_file(self,file_name):
        fh = open(file_name, 'w')
        strbar = self._addbar()
        strstr = self._addstr()
        strcon = self._addcon()
        print(self.strcounter)
        # stract = self._addact([1,2])
        stract = self._addact()
        # contents = strbar + strstr + strcon + self.rem
        contents = strbar + strstr + strcon + stract+ self.rem
        fh.write(contents)
        fh.close()



a = tenseg_skeleton('.\py.mat')
# print(a._addbar())
a.save_to_file('test2.xml')

# a.write('test.xml')