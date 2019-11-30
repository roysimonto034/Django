from django.shortcuts import render


def tableview(request):
    data=['Name','Org','addr']
    val1=('Amit','Dell','Delhi')
    val2=('Sukhbir','ENY','BLR')
    val3=('Shivani','PWC','CCU')
    val4=('Meetu','KPMG','MUMB')
    dcp={'nm':data[0],'og':data[1],'ad':data[2],'v1':val1[0],'v2':val1[1],'v3':val1[2],'g1':val2[0],'g2':val2[1],'g3':val2[2]}
    return render(request,'secondapp/tabledemo.html',context=dcp)
# Create your views here.
