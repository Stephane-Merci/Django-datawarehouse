from django.shortcuts import render
from django.db.models import Sum
from .models import *
from django.db import connection
import calendar

# Create your views here.
def chart1(request):

    if request.method == 'POST':
        month = request.POST.get("month")
    else:
        month = 1
    with connection.cursor() as cursor:
        # cursor.execute("SELECT TOWN, MONTH, YEAR, ITEM_TYPE, WAREHOUSE_SALES FROM alcohol WHERE MONTH = 1")  # Raw SQL
        cursor.execute(f"SELECT TOWN, ITEM_TYPE, FLOOR(SUM(WAREHOUSE_SALES)) AS TOTAL_QUANTITY FROM alcohol WHERE MONTH = {month} GROUP BY TOWN, ITEM_TYPE ORDER BY TOWN, TOTAL_QUANTITY DESC;")  # Raw SQL
        raw_data = cursor.fetchall()
        results = list(raw_data)
        
        town = []
        total_order = [0,0,0,0]
        item_type = []
        data0 = [0,0,0,0,0]
        data1 = [0,0,0,0,0]
        data2 = [0,0,0,0,0]
        data3 = [0,0,0,0,0]
        
        
        for row in results:
            if row[0] not in town:
                town.append(row[0])
            if row[1] not in item_type:
                item_type.append(row[1])
            
        for row in results:
            if row[0] == town[0]:    
                total_order[0] += row[2]
            if row[0] == town[1]:    
                total_order[1] += row[2]
            if row[0] == town[2]:    
                total_order[2] += row[2]
            if row[0] == town[3]:    
                total_order[3]+= row[2]
        
        for row in results:
            if row[0] == town[0]:
                if row[1]  == item_type[0]:
                    data0[0] += row[2]
                if row[1]  == item_type[1]:
                    data0[1] += row[2]
                if row[1]  == item_type[2]:
                    data0[2] += row[2]
                if row[1]  == item_type[3]:
                    data0[3] += row[2]
                if row[1]  == item_type[4]:
                    data0[4] += row[2]
                    
            if row[0] == town[1]:
                if row[1]  == item_type[0]:
                    data1[0] += row[2]
                if row[1]  == item_type[1]:
                    data1[1] += row[2]
                if row[1]  == item_type[2]:
                    data1[2] += row[2]
                if row[1]  == item_type[3]:
                    data1[3] += row[2]
                if row[1]  == item_type[4]:
                    data1[4] += row[2]
                    
            if row[0] == town[2]:
                if row[1]  == item_type[0]:
                    data2[0] += row[2]
                if row[1]  == item_type[1]:
                    data2[1] += row[2]
                if row[1]  == item_type[2]:
                    data2[2] += row[2]
                if row[1]  == item_type[3]:
                    data2[3] += row[2]
                if row[1]  == item_type[4]:
                    data2[4] += row[2]
                    
            if row[0] == town[3]:
                if row[1]  == item_type[0]:
                    data3[0] += row[2]
                if row[1]  == item_type[1]:
                    data3[1] += row[2]
                if row[1]  == item_type[2]:
                    data3[2] += row[2]
                if row[1]  == item_type[3]:
                    data3[3] += row[2]
                if row[1]  == item_type[4]:
                    data3[4] += row[2]
            
        print(town, total_order,item_type)
            
            
        
        context = {
            'data': results,
            'town':town,
            'total_order':total_order,
            'item_type':item_type,
            'data0':data0,
            'data1':data1,
            'data2':data2,
            'data3':data3,
            'month' : month,
            }
    return render(request, 'core/chart.html', context)

def chart2(request):

    if request.method == 'POST':
        town = request.POST.get("town")
    else:
        town = "Bafoussam"
    with connection.cursor() as cursor:
        # cursor.execute("SELECT TOWN, MONTH, YEAR, ITEM_TYPE, WAREHOUSE_SALES FROM alcohol WHERE MONTH = 1")  # Raw SQL
        cursor.execute(f"SELECT ITEM_TYPE, MONTH, FLOOR(SUM(WAREHOUSE_SALES)) AS TOTAL_QUANTITY FROM alcohol WHERE TOWN = '{town}' GROUP BY ITEM_TYPE, MONTH ORDER BY MONTH DESC;")  # Raw SQL
        raw_data = cursor.fetchall()
        results = list(raw_data)
        
        item_type = []
        total_order = [0,0,0,0,0]
        month = []
        data0 = [0,0,0,0,0,0,0,0,0,0,0,0]
        data1 = [0,0,0,0,0,0,0,0,0,0,0,0]
        data2 = [0,0,0,0,0,0,0,0,0,0,0,0]
        data3 = [0,0,0,0,0,0,0,0,0,0,0,0]
        data4 = [0,0,0,0,0,0,0,0,0,0,0,0]
        
        
        for row in results:
            if row[0] not in item_type:
                item_type.append(row[0])
            if row[1] not in month:
                month.append(row[1])
        # print(month.sort())
        # month = month.sort()
        
        for row in results:
            if row[0] == item_type[0]:    
                total_order[0] += row[2]
            if row[0] == item_type[1]:    
                total_order[1] += row[2]
            if row[0] == item_type[2]:    
                total_order[2] += row[2]
            if row[0] == item_type[3]:    
                total_order[3]+= row[2]
            if row[0] == item_type[4]:    
                total_order[4]+= row[2]
        
        for row in results:
            if row[0] == item_type[0]:
                for i in range(len(month)):
                    if row[1]  == month[i]:
                        data0[i] += row[2]
                    
            if row[0] == item_type[1]:
                for i in range(len(month)):
                    if row[1]  == month[i]:
                        data1[i] += row[2]
                    
            if row[0] == item_type[2]:
                for i in range(len(month)):
                    if row[1]  == month[i]:
                        data2[i] += row[2]
                    
            if row[0] == item_type[3]:
                for i in range(len(month)):
                    if row[1]  == month[i]:
                        data3[i] += row[2]
                    
            if row[0] == item_type[4]:
                for i in range(len(month)):
                    if row[1]  == month[i]:
                        data4[i] += row[2]
            
        print(len(month), total_order,item_type)
            
            
        
        context = {
            'data': results,         
            'item_type':item_type,
            'total_order':total_order,
            'month':month,
            'data0':data0,
            'data1':data1,
            'data2':data2,
            'data3':data3,
            'data4':data4,
            'town' : town,
            }
    return render(request, 'core/chart2.html', context)


def chart3(request):

    if request.method == 'POST':
        item_type = request.POST.get("item_type")
    else:
        item_type = "BEER"
    with connection.cursor() as cursor:
        # cursor.execute("SELECT TOWN, MONTH, YEAR, ITEM_TYPE, WAREHOUSE_SALES FROM alcohol WHERE MONTH = 1")  # Raw SQL
        cursor.execute(f"SELECT TOWN, MONTH, FLOOR(SUM(WAREHOUSE_SALES)) AS TOTAL_QUANTITY FROM alcohol WHERE ITEM_TYPE = '{item_type}' GROUP BY TOWN, MONTH ORDER BY MONTH DESC;")  # Raw SQL
        raw_data = cursor.fetchall()
        results = list(raw_data)
        
        town = []
        total_order = [0,0,0,0]
        month = []
        data0 = [0,0,0,0,0,0,0,0,0,0,0,0]
        data1 = [0,0,0,0,0,0,0,0,0,0,0,0]
        data2 = [0,0,0,0,0,0,0,0,0,0,0,0]
        data3 = [0,0,0,0,0,0,0,0,0,0,0,0]
        
        
        for row in results:
            if row[0] not in town:
                town.append(row[0])
            if row[1] not in month:
                month.append(row[1])
        # print(month.sort())
        # month = month.sort()
        
        for row in results:
            if row[0] == town[0]:    
                total_order[0] += row[2]
            if row[0] == town[1]:    
                total_order[1] += row[2]
            if row[0] == town[2]:    
                total_order[2] += row[2]
            if row[0] == town[3]:    
                total_order[3]+= row[2]
        
        for row in results:
            if row[0] == town[0]:
                for i in range(len(month)):
                    if row[1]  == month[i]:
                        data0[i] += row[2]
                    
            if row[0] == town[1]:
                for i in range(len(month)):
                    if row[1]  == month[i]:
                        data1[i] += row[2]
                    
            if row[0] == town[2]:
                for i in range(len(month)):
                    if row[1]  == month[i]:
                        data2[i] += row[2]
                    
            if row[0] == town[3]:
                for i in range(len(month)):
                    if row[1]  == month[i]:
                        data3[i] += row[2]
            
        print(month, total_order,item_type)
            
            
        
        context = {
            'data': results,  
            'town' : town,       
            'total_order':total_order,
            'month':month,
            'data0':data0,
            'data1':data1,
            'data2':data2,
            'data3':data3,
            'item_type':item_type,
            }
    return render(request, 'core/chart3.html', context)
