# -*- coding: utf-8 -*-
__author__ = 'prm14'

import csv
import cPickle


# 统计item_feature，降序排列编码
# 序列化结果
class EncodeClass:
	def __init__(self):
		# item, category, level 1 category, brand, supplier
		self.user_dict = {}
		self.user_list = []
		self.merchant_dict = {}
		self.merchant_list = []
		self.location_dict = {}
		self.location_list = []

	def encode(self):
		itt = {}
		stot = {}
		cat = {}
		cat1 = {}
		brt = {}
		supt = {}

		reader = csv.reader(open("data/item_store_feature1.csv"))
		for record in reader:
			target = long(float(record[30]))
			item_id = record[1]
			store_id = record[2]
			cate_id = record[3]
			cate1_id = record[4]
			brand_id = record[5]
			supplier_id = record[6]

			itt.setdefault(item_id, 0.0)
			itt[item_id] += target
			stot.setdefault(store_id, 0.0)
			stot[store_id] += target
			cat.setdefault(cate_id, 0.0)
			cat[cate_id] += target
			cat1.setdefault(cate1_id, 0.0)
			cat1[cate1_id] += target
			brt.setdefault(brand_id, 0.0)
			brt[brand_id] += target
			supt.setdefault(supplier_id, 0.0)
			supt[supplier_id] += target

		print 'statistic result: '
		print 'item:\t%d\r\nstore:\t%d\r\ncategory:\t%d\r\ncategory1:\t%d\r\nbrand:\t%d\r\nsupplier:\t%d\r\n' % (
			len(itt), len(stot), len(cat), len(cat1), len(brt), len(supt))
		# 按频数降序排列
		self.item_list = [k for k, v in sorted(itt.iteritems(), key=lambda d: d[1], reverse=True)]
		self.store_list = [k for k, v in sorted(stot.iteritems(), key=lambda d: d[1], reverse=True)]
		self.cate_list = [k for k, v in sorted(cat.iteritems(), key=lambda d: d[1], reverse=True)]
		self.cate1_list = [k for k, v in sorted(cat1.iteritems(), key=lambda d: d[1], reverse=True)]
		self.brand_list = [k for k, v in sorted(brt.iteritems(), key=lambda d: d[1], reverse=True)]
		self.supplier_list = [k for k, v in sorted(supt.iteritems(), key=lambda d: d[1], reverse=True)]

		self.item_dict = dict.fromkeys(self.item_list, 0)
		for i in range(len(self.item_list)):
			self.item_dict[self.item_list[i]] = i
		self.store_dict = dict.fromkeys(self.store_list, 0)
		for i in range(len(self.store_list)):
			self.store_dict[self.store_list[i]] = i
		self.cate_dict = dict.fromkeys(self.cate_list, 0)
		for i in range(len(self.cate_list)):
			self.cate_dict[self.cate_list[i]] = i
		self.cate1_dict = dict.fromkeys(self.cate1_list, 0)
		for i in range(len(self.cate1_list)):
			self.cate1_dict[self.cate1_list[i]] = i
		self.brand_dict = dict.fromkeys(self.brand_list, 0)
		for i in range(len(self.brand_list)):
			self.brand_dict[self.brand_list[i]] = i
		self.supplier_dict = dict.fromkeys(self.supplier_list, 0)
		for i in range(len(self.supplier_list)):
			self.supplier_dict[self.supplier_list[i]] = i

		self.save_pickle('item_list')
		self.save_pickle('item_dict')
		self.save_pickle('store_list')
		self.save_pickle('store_dict')
		self.save_pickle('cate_list')
		self.save_pickle('cate_dict')
		self.save_pickle('cate1_list')
		self.save_pickle('cate1_dict')
		self.save_pickle('brand_list')
		self.save_pickle('brand_dict')
		self.save_pickle('supplier_list')
		self.save_pickle('supplier_dict')

	def load_all(self):
		self.load_pickle('item_list')
		self.load_pickle('item_dict')
		self.load_pickle('store_list')
		self.load_pickle('store_dict')
		self.load_pickle('cate_list')
		self.load_pickle('cate_dict')
		self.load_pickle('cate1_list')
		self.load_pickle('cate1_dict')
		self.load_pickle('brand_list')
		self.load_pickle('brand_dict')
		self.load_pickle('supplier_list')
		self.load_pickle('supplier_dict')

	def save_pickle(self, filename):
		f = file('data/' + filename + '.pickle', 'w')
		cPickle.dump(getattr(self, filename), f)
		f.close()

	def load_pickle(self, filename):
		f = file('data/' + filename + '.pickle')
		setattr(self, filename, cPickle.load(f))
		f.close()
		print 'load %d records of ' % len(getattr(self, filename)), filename, ' done.'
		return getattr(self, filename)
